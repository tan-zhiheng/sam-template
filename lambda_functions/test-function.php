<?php

use Bref\Context\Context;
use Aws\S3\S3Client;

require __DIR__ . '/../vendor/autoload.php';

// Bootstrap the Laravel application
$app = require __DIR__ . '/../bootstrap/app.php';

// Bootstrapping the Laravel kernel so that environment variables are loaded
$app->make(Illuminate\Contracts\Http\Kernel::class)->bootstrap();


return function ($event, Context $context) {
    echo json_encode($event), PHP_EOL;
    $s3Client = new S3Client([
        'region'  => env('AWS_REGION'),
		'version' => 'latest',
    ]);
    $result = $s3Client->listBuckets();
    echo json_encode($result['Buckets']), PHP_EOL;
};

