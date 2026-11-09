<?php

declare(strict_types=1);

namespace GardusiGustavo\Package\Tests;

use GardusiGustavo\Package\Answer;
use PHPUnit\Framework\TestCase;

final class AnswerTest extends TestCase
{
    public function testAnswerIs42(): void
    {
        self::assertSame(42, Answer::value());
    }
}
