FROM bref/php-82 as builder

COPY composer.dev.json /var/task/composer.json

RUN cd /var/task && \
    curl -s https://getcomposer.org/installer | php && \
    php composer.phar install --no-dev --optimize-autoloader

FROM bref/php-82 as app
COPY --from=builder /var/task/vendor /var/task/vendor
COPY --from=builder /var/task/composer.json /var/task/composer.json
COPY app /var/task/app
COPY bootstrap /var/task/bootstrap
COPY config /var/task/config
COPY database /var/task/database
COPY routes /var/task/routes
COPY lambda_functions /var/task/lambda_functions
COPY .env artisan /var/task

## AWS Lambda filesystem is read-only (except /tmp),
## so, for Laravel, we should update various writeable
## paths to point to location inside of it.
## On initialization, function's bootstrap script will
## create these folders, so we just tweak them via environment variables.
ENV APP_PACKAGES_CACHE /tmp/packages.php
ENV APP_SERVICES_CACHE /tmp/services.php
ENV APP_CONFIG_CACHE /tmp/config.php
ENV APP_ROUTES_CACHE /tmp/routes.php
ENV APP_EVENTS_CACHE /tmp/events.php

CMD ["lambda_functions/test-function.php"]
