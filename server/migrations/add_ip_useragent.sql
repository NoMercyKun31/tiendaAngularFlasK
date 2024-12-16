ALTER TABLE pedidos
ADD COLUMN ip_address VARCHAR(45) NULL COMMENT 'IPv4 or IPv6 address',
ADD COLUMN user_agent VARCHAR(255) NULL COMMENT 'Browser User-Agent string';
