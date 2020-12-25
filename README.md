# Api_For_heart_disease_model
-It a api for my ML model
# How to run ?
-Git clone the files<br>
-Open console and run app.py<br>
--python app.py<br>
# More deatils 
<!doctype html>
<html lang="en">
  <body class="bg-color">
    <div class="container p-5">
        <div class="card p-5">
            <h1 class="bold text-secondary monts-bold mb-0 pb-0">Healthy Heart</h1>
            <h5 class="text-success monts-700">INTRODUCTION</h5>
            <p class="text-justify">
                Healthy Heart is an Unofficial heart disease classification API. It take the health related data like age,cestpain,calories and etc and classifies it as the paitents has heart desies or not. <br><br> This an free api service so enjoy it. And that's what this API saves you of. ;) <br><br> <b>Notice:</b> Healthy Heart does not support authenticated requests. You can not update your paitent list.
            </p>
            <p style="font-size: 16px;">
               <b>API Path: </b><span class="border-normal p-1">http://127.0.0.1:5300/api/predict</span>
            </p>
            <p style="font-size: 16px;">
                <b>API Version: </b><span class="border-normal p-1">v1.0</span>
            </p>
            <br>
            <h5 class="text-success monts-700">HTTP Response</h5>
            <ul>
                <li>
                    <p class="text-justify">200 <span class="border-normal p-1">OK</span> - the request was successful.</p>
                </li>
                <li>
                    <p class="text-justify">304 <span class="border-normal p-1">Not Modified</span>- You have the latest data</p>
                </li>
                <li>
                    <p class="text-justify">400 <span class="border-normal p-1">Bad Request</span> - You’ve made an invalid request</p>
                </li>
                <li>
                    <p class="text-justify">404 <span class="border-normal p-1">Not Found</span> - Resource not found.</p>
                </li>
                <li>
                    <p class="text-justify">405 <span class="border-normal p-1">Method Not Allowed</span> - requested method is not supported for resource</p>
                </li>
                <li>
                    <p class="text-justify">500 <span class="border-normal p-1">Internal Server Error</span> - Something is not working on our end</p>
                </li>
                <li>
                    <p class="text-justify">503 <span class="border-normal p-1">Service Unavailable</span> - Something is not working on server down</p>
                </li>
            </ul>
  </body>
</html>
