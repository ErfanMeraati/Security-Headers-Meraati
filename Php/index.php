<?php
// Add security headers
header("Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none';");
header("X-Frame-Options: DENY");
header("X-Content-Type-Options: nosniff");
header("Strict-Transport-Security: max-age=31536000; includeSubDomains");
header("Referrer-Policy: no-referrer");

// Example page content
echo "Hello, Secure World!";
?>
