drop table if exists posts2;
	create table posts2 (
		id integer primary key autoincrement,
		name text not null,
		content text not null
);
