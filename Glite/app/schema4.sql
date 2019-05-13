drop table if exists posts4;
	create table posts4 (
		id integer primary key autoincrement,
		name text not null,
		content text not null
);
