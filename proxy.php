<?php
if (!isset($_GET['url']) || empty($_GET['url'])) {
    die("Error: No URL provided.");
}

$url = $_GET['url'];

// Validate URL format
if (!filter_var($url, FILTER_VALIDATE_URL)) {
    die("Error: Invalid URL format.");
}

// Fetch content from the requested URL
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
$response = curl_exec($ch);
$http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);

if ($http_code >= 400) {
    die("Error: Unable to fetch the requested URL. HTTP code $http_code.");
}

curl_close($ch);

// Display the content to the user
echo $response;
?>
