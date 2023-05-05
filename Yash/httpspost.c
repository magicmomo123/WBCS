HTTPClient http;

  // Set content type header
  http.addHeader("Content-Type", "application/octet-stream");

  // Convert integer array to byte array
  byte byteArray = (byte)myArray;

  // Send POST request
  int httpResponseCode = http.POST(serverUrl, byteArray, sizeof(myArray));

  // Check HTTP response
  if (httpResponseCode > 0) {
    Serial.printf("HTTP response code: %d\n", httpResponseCode);
    String payload = http.getString();
    Serial.println(payload);
  } else {
    Serial.printf("HTTP request failed with error code %d\n", httpResponseCode);
  }

  // Close HTTP client
  http.end();
}
