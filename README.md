# Api_For_heart_disease_model
-It a api for my ML model
# How to run ?
-Git clone the files<br>
-Open console and run app.py<br>
--python app.py<br>
# More deatils 
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;500;600;700;900&display=swap" rel="stylesheet">
    <title>Healthy Heart</title>
    <style>
        *{
            font-family: 'Montserrat', sans-serif;
        }
        .monts-bold{
            font-weight: 900;
        }
        .monts-500{
            font-weight: 500;
        }
        .monts-700{
            font-weight: 700;
        }
        hr{
            border: 1px solid #000000;
        }
        .bg-color{
            background-image: linear-gradient(to right, #5195a5 , #1965b5);
        }
        .border-normal{
            border: 1px solid #1e357e;
            background-color: #92a4ca6e;
        }
    </style>
  </head>
  <body class="bg-color">
    <div class="container p-5">
        <div class="card p-5">
            <h1 class="bold text-secondary monts-bold mb-0 pb-0">Healthy Heart</h1><hr>
            <h5 class="text-success monts-700">INTRODUCTION</h5>
            <p class="text-justify">
                Healthy Heart is an Unofficial heart disease classification API. It take the health related data like age,cestpain,calories and etc and classifies it as the paitents has heart desies or not. <br><br> This an free api service so enjoy it. And that's what this API saves you of. ;) <br><br> <b>Notice:</b> Healthy Heart does not support authenticated requests. You can not update your paitent list.
            </p>
            <p style="font-size: 16px;">
               <b>API Path: </b><span class="border-normal p-1">http://127.0.0.1:5300/api/classify</span>
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

            <h5 class="text-success monts-700">REFERENCE</h5>
            <p class="text-justify">
                This path <b>api/classify</b> only takes <b>POST</b> request.
            </p>
            <h2 class="text-secondray monts-500"><b>Parameter & Description</b></h2>
            <table class="table">
                <thead class="thead-dark">
                  <tr>
                    <th scope="col">Parameter</th>
                    <th scope="col">Description</th>
                    <th scope="col">Variables</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Age</td>
                    <td>Patient’s age in completed years </td>
                    <td>age</td>
                  </tr>
                  <tr>
                    <td>Sex</td>
                    <td>Patient’s Gender (male represented as1 and fe-male as 0)</td>
                    <td>sex</td>
                  </tr>
                  <tr>
                    <td>Cerebral Palsy</td>
                    <td>The type of Chest pain categorized into 4 values: <br> 1. typical angina, 2. atypical angina, 3. non-anginal pain and 4. asymptomatic</td>
                    <td>cp</td>
                  </tr>
                  <tr>
                      <td>Resting Blood Pressure</td>
                      <td>Level of blood pressure at resting mode (inmm/Hg at the time of admitting in the hospital)</td>
                      <td>trestbps</td>
                  </tr>
                  <tr>
                      <td>Cholestrol</td>
                      <td>Serum cholesterol in mg/dl</td>
                      <td>chol</td>
                  </tr>
                  <tr>
                      <td>Fasting Blood Sugar</td>
                      <td>Blood sugar levels on fasting > 120 mg/dl; repre-sented as 1 in case of true, and 0 in case of false</td>
                      <td>fbs</td>
                  </tr>
                  <tr>
                      <td>Restecg</td>
                      <td>Results of electrocardiogram while at rest arerepresented in 3 distinct values: Normal stateis represented as Value 0, Abnormality in ST-Twave as Value 1, (which may include inversionsof T-wave and/or depression or elevation of STof > 0.05 mV) and any probability or certaintyof LV hypertrophy by Estes’ criteria as Value 2</td>
                      <td>restecg</td>
                  </tr>
                  <tr>
                      <td>Thalach</td>
                      <td>The accomplishment of the maximum rate ofheart</td>
                      <td>thalach</td>
                  </tr>
                  <tr>
                      <td>Exang</td>
                      <td>Angina induced by exercise. ( 0 depicting ‘no’and 1 depicting ‘yes’)</td>
                      <td>exang</td>
                  </tr>
                  <tr>
                      <td>Oldpeak</td>
                      <td>Exercise-induced ST depression in comparisonwith the state of rest</td>
                      <td>oldpeak</td>
                  </tr>
                  <tr>
                      <td>Slope</td>
                      <td>ST segment measured in terms of the slope dur-ing peak exercise depicted in three values: 1.unsloping, 2. ﬂat and 3. downsloping</td>
                      <td>slope</td>
                  </tr>
                  <tr>
                      <td>Ca</td>
                      <td>Fluoroscopy coloured major vessels numberedfrom 0 to 3</td>
                      <td>ca</td>
                  </tr>
                  <tr>
                      <td>Thal</td>
                      <td>Status of the heart illustrated through three dis-tinctly numbered values. Normal numbered as 3,ﬁxed defect as 6 and reversible defect as 7.</td>
                      <td>thal</td>
                  </tr>
                  <tr>
                      <td>Result</td>
                      <td>Heart disease diagnosis represented in 2 values,with 0 indicating total absence and 1 indicating the presence in of heart deasies.</td>
                      <td>result</td>
                  </tr>
                </tbody>
              </table>
        </div>
    </div>


    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
  </body>
</html>
