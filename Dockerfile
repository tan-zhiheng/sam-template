FROM bref/php-82 as builder

COPY composer.dev.json /var/task/composer.json

RUN cd /var/task && \
    curl -s https://getcomposer.org/installer | php && \
    php composer.phar install --no-dev --optimize-autoloader

FROM bref/php-82 as app
COPY --from=builder /var/task/vendor /var/task/vendor
COPY app /var/task/app
COPY bootstrap /var/task/bootstrap
COPY config /var/task/config
COPY database /var/task/database
COPY routes /var/task/routes
COPY lambda_functions /var/task/lambda_functions
COPY .env artisan /var/task
CMD ["lambda_functions/test-function.php"]
