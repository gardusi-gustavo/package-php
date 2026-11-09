<?php

declare(strict_types=1);

require __DIR__ . '/../../vendor/autoload.php';

use GardusiGustavo\Package\Answer;

header('Content-Type: application/json');
echo json_encode(['answer' => Answer::value()], JSON_THROW_ON_ERROR);
