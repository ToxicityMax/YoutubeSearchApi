FROM nginx

# Remove the default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf

#Replace with our own nginx config
COPY nginx.conf /etc/nginx/conf.d
