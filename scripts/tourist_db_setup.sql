drop database if exists tourist_db;
create database tourist_db;

\c tourist_db

drop schema if exists public cascade;
create schema public;

create table users (
	user_id uuid primary key default gen_random_uuid(),
	name varchar (100) not null,
	email varchar (255) unique not null,
	hashed_password varchar (128) not null,
	registration_date timestamp default current_timestamp
);

create table countries (
	country_id serial primary key,
	name varchar (100) not null
);

create table cities (
	city_id serial primary key,
	name varchar (100) not null,
	country_id int not null,
	-- foreign keys definition
	constraint fk_country_id foreign key (country_id)
		references countries (country_id)
		on delete cascade
		on update cascade
);

create table posts (
	post_id serial primary key,
	title varchar (255) not null,
	description text not null,
	creation_date timestamp default current_timestamp,
	city_id int not null,
	user_id uuid not null,
	-- foreign keys definition
	constraint fk_city_id foreign key (city_id)
		references cities (city_id)
		on delete cascade
		on update cascade,
	constraint fk_user_id foreign key (user_id)
		references users (user_id)
		on delete cascade
		on update cascade
);

create table images (
	image_id serial primary key,
	url text not null,
	post_id int not null,
	-- foreign keys definition
	constraint fk_post_id foreign key (post_id)
		references posts (post_id)
		on delete cascade
		on update cascade
);

create table tags (
	tag_id serial primary key,
	name varchar (50) not null
);

create table post_tags (
	post_tag_id serial primary key,
	post_id int not null,
	tag_id int not null,
	-- foreign keys definition
	constraint fk_post_id foreign key (post_id)
		references posts (post_id)
		on delete cascade
		on update cascade,
	constraint fk_tag_id foreign key (tag_id)
		references tags (tag_id)
		on delete cascade
		on update cascade
);

create table comments (
	comment_id serial primary key,
	content text not null,
	comment_date timestamp default current_timestamp,
	user_id uuid not null,
	post_id int not null,
	-- foreign keys definition
	constraint fk_user_id foreign key (user_id)
		references users (user_id)
		on delete cascade
		on update cascade,
	constraint fk_post_id foreign key (post_id)
		references posts (post_id)
		on delete cascade
		on update cascade
);