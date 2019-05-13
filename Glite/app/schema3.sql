drop table if exists posts3;
	create table posts3 (
		id integer primary key autoincrement,
		name text not null,
		content text not null
);
