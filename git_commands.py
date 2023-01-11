git init
git add .
git add file_name.ext
git commit -m "message_optional" -m "description_optional"
git status
git remote add origin "ssh_link"
git remote -v
git push -u origin master # -u defines the upstream, afterwards only git push
git push
git 


## to link the local machine with github using ssh
eval "$(ssh-agent -s)" # to start an ssh agent in background
ssh-add ~/.ssh/zahir_ssh # zahir_ssh = name of the dir where public key

#branching 
git branch
git checkout -b branch_name # to create and switch between branches

