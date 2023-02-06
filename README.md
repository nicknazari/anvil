#The plan now:

Express should be super easy to integrate with the lambda function HTTP endpoints. We should probably opt for that over Flask, as all of the front end is written in JS/HTML/CSS, and HTML has super simple default integration with Express. 

Sending data with HTML/Express is literally 

<form action="function_name" method="get/put/post/delete"> <input> Everyting in these tags is sent as JSON to an Express method named "function_name" </input> </form>

