create table if not exists users (
id int AUTO_INCREMENT primary key,
username varchar(50) not null unique,
password varchar(255) not null,
created_at timestamp default CURRENT_TIMESTAMP
);

insert into users (username, password) values ('pao1', 'pass1' );
insert into users (username, password) values ('pao2', 'pass2' );
insert into users (username, password) values ('pao3', 'pass3' );




