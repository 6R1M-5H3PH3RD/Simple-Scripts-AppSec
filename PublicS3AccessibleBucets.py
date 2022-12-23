#This script uses the boto3 library to connect to the S3 service and list all S3 buckets in your account. It then checks the access control list (ACL) for each bucket to see if the "PublicRead" permission is granted to the "AllUsers" group. If this permission is found, the script prints a message indicating that the bucket is publicly accessible. If the permission is not found, the script prints a message indicating that the bucket is not publicly accessible.
#for scanning publicly available S3 buckets to suit your specific needs:
#Handle different types of permissions: Currently, the script only checks for the "PublicRead" permission. You can modify the script to check for other types of permissions, such as "PublicWrite" or "PublicReadWrite", by adding additional conditions to the if statement.
#Check for specific grantees: Currently, the script only checks for the "AllUsers" group as the grantee. You can modify the script to check for other grantees, such as specific Amazon S3 users or AWS accounts, by modifying the if statement to compare the Grantee field with the desired grantee.
#Check bucket properties: You can modify the script to check additional properties of the bucket, such as the bucket's location or the versioning status. To do this, you can use the s3.get_bucket_location and s3.get_bucket_versioning functions, respectively.
#Check bucket contents: You can modify the script to check the contents of the bucket for specific files or patterns. To do this, you can use the s3.list_objects function to list the objects in the bucket, and then iterate through the objects to check for the desired files or patterns.




import boto3

# Connect to the S3 service
s3 = boto3.client('s3')

# List all S3 buckets
response = s3.list_buckets()
buckets = response['Buckets']

# Check the permissions on each bucket
for bucket in buckets:
  bucket_name = bucket['Name']
  bucket_acl = s3.get_bucket_acl(Bucket=bucket_name)
  
  # Check for the "PublicRead" permission in the bucket ACL
  for grant in bucket_acl['Grants']:
    if grant['Permission'] == 'READ' and grant['Grantee']['URI'] == 'http://acs.amazonaws.com/groups/global/AllUsers':
      print(f'Publicly accessible bucket found: {bucket_name}')
      break
  else:
    print(f'Bucket not publicly accessible: {bucket_name}')

  # Check for specific permissions and grantees
  public_read = False
  public_write = False
  specific_grantee = False
  for grant in bucket_acl['Grants']:
    if grant['Permission'] == 'READ' and grant['Grantee']['URI'] == 'http://acs.amazonaws.com/groups/global/AllUsers':
      public_read = True
    elif grant['Permission'] == 'WRITE' and grant['Grantee']['URI'] == 'http://acs.amazonaws.com/groups/global/AllUsers':
      public_write = True
    elif grant['Grantee']['ID'] == '012345678901':
      specific_grantee = True

  # Print a message based on the permissions and grantees found
  if public_read and public_write:
    print(f'Publicly accessible bucket with read/write permissions found: {bucket_name}')
  elif public_read:
    print(f'Publicly accessible bucket with read-only permissions found: {bucket_name}')
  elif specific_grantee:
    print(f'Bucket accessible by specific grantee: {bucket_name}')
  else:
    print(f'Bucket not publicly accessible: {bucket_name}')

# Check the bucket properties for each bucket
for bucket in buckets:
  bucket_name = bucket['Name']
  location = s3.get_bucket_location(Bucket=bucket_name)
  versioning = s3.get_bucket_versioning(Bucket=bucket_name)
  print(f'Bucket {bucket_name}: location={location["LocationConstraint"]}, versioning={versioning["Status"]}')

# Check the bucket contents for specific files or patterns
for bucket in buckets:
  bucket_name = bucket['Name']
  objects = s3.list_objects(Bucket=bucket_name)
  for obj in objects['Contents']:
    key = obj['Key']
    if key.endswith('.txt') or 'secret' in key:
      print(f'Sensitive file or pattern found in bucket {bucket_name}: {key}')

#This updated script now includes checks for different types of permissions and grantees, as well as checks for bucket properties and contents. You can further modify the script to suit your specific needs. For example, you could add additional conditions to the if statements or add additional functions to check for other bucket properties or contents.
# TODO: Write a function which can saves the results in an HTML table
