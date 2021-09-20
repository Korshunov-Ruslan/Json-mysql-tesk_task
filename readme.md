The task was: 
1. Make CRUD with mysqldb.
2. Update user with some conditions.
3. We need to accept an array of data and update the file for which this array came, if the file is not specified, then we do not update anything, if it is specified, but does not exist, we create it. External access will only be via ru-RU or en-GB, without .json
4. Take a photo to the /friendship/magic/photo folder if its size does not exceed one megabyte.

=========
How to check if the code works?
1. Git clone that repo 
2. Download https://insomnia.rest or smth like that 
3. Configure the file "app.py" (line 10) 
4. Run "startapp.py"
5. Make a POST / GET / PUT / DELETE  requests via insomnia (route for that requests you can find in task1,2,3,4.py)
