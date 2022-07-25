create table url
(
	code varchar not null,
	url varchar not null,
	created timestamp default now() not null,
	modified timestamp default now() not null
);

comment on table url is 'source urls and short codes';

comment on column url.code is 'short code';

comment on column url.url is 'source url';


create unique index url_code_uindex
	on url (code);

create index url_code__index
	on url (code);

create unique index url_url_uindex
	on url (url);

alter table url
	add constraint url_pk
		primary key (code);

create table transition
(
	code varchar not null,
	id serial,
	datetime timestamp default now() not null
);

comment on table transition is 'url transitions map';

create index transition_code__index
	on transition (code);

create index transition_datetime_index
	on transition (datetime desc);

create unique index transition_id_uindex
	on transition (id);

alter table transition
	add constraint transition_pk
		primary key (id);

alter table transition
	add constraint transition_url_code_fk
		foreign key (code) references url
			on update cascade on delete cascade;