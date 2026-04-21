Question 2:Infrastructure As Code
Solution:
Step 1: Remove the resource from State
	terraform state rm 'aws_ec2_instance.name[1]' //Assume "2nd" resource as index 1

Step 2: Update your configuration by replacing count with for_each	//for_each uses unique keys rather than numerical indexes

Step 3: Use a moved block	//It tells Terraform that the resource previously known as name[0] is now name["key1"].
	moved {
  from = aws_ec2_instance.name[0]
  to   = aws_ec2_instance.name["key1"]
}

Commands Used:
1. Check Current State		terraform state list
2. Remove from Management	terraform state rm <resource>[index]
3. Preview Changes		terraform plan
4. Apply state file 		terraform apply
