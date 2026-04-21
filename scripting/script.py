Question 1:Scripting
Solution: Python Script:
      
       if 'delete' in action:		//Block any 'delete' 
            sys.exit(f"REJECTED: {addr} scheduled for destruction.")

       if 'update' in action:		//For updates, ensure only 'tags' changed, and only 'GitCommitHash' within tags
              if any(before.get(k) != after.get(k) for k in set(before) | set(after) if k != 'tags'):		//Checking top-level attributes excluding 'tags'
                sys.exit(f"REJECTED: {addr} modifies non-tag attributes.")
            
            
            bt, at = before.get('tags', {}), after.get('tags', {})		//Checking nested tags excluding 'GitCommitHash'
            if any(bt.get(t) != at.get(t) for t in set(bt) | set(at) if t != 'GitCommitHash'):
                sys.exit(f"REJECTED: {addr} modifies forbidden tags.")

    print("SUCCESS: Plan is safe."); sys.exit(0)

Summary of Result Actions:
1. New Resources		Proceed with terraform apply.
2. Only GitCommitHash 		Proceed with terraform apply.
3. Resource Deletion		Manual review for any infrastructure .risks
