# Imagen base de Alpine con HAProxy instalado
FROM haproxy:alpine

# Copiar el archivo haproxy.cfg en la imagen
COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg

# Exponer el puerto 80
EXPOSE 80

# Iniciar HAProxy
CMD ["haproxy", "-f", "/etc/haproxy/haproxy.cfg"]
