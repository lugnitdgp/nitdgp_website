# Prevent simultaneous requests from a specific IP

This is used in the `/faculty/notes/` view to prevent some attempts to run a
bruteforce attack.

Copy the following line into the `http` block in `nginx.conf`:

    limit_req_zone $binary_remote_addr zone=xlimit:5m rate=5r/s;

Then add the following line for the specific URL you want to protect which in
our case is `faculty/notes/`:

    location /faculty/notes/ {
        ...
        limit_req zone=xlimit;
        include proxy_params; # Pass it to gunicorn as we are using django
        proxy_pass http://unix:/run/gunicorn.sock;
        ....
    }


# Prevent requesting a specific URI

This can be used to protect actual information from being retrived directly or
without authentication:

    location /files/faculty/notes/ {
        deny all;
    }

The above is used in our case to prevent direct access of actual notes that a
faculty might have uploaded.
