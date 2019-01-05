/* create table: products & categories */
create table products(id integer primary key autoincrement, name, category_id);
create table categories(id integer primary key autoincrement, name);

/* insert values for products & categories*/
insert into products(name, category_id) values ('Sampo', 1);
insert into products(name, category_id) values ('Sikat Gigi', 1);
insert into products(name, category_id) values ('Indonmie goreng spesial', 2);
insert into products(name, category_id) values ('mie sedap soto', 2);
insert into products(name, category_id) values ('rock mie baso', 2);
insert into products(name, category_id) values ('Nuget', 3);
insert into categories(name) values ('Peralatan Mandi');
insert into categories(name) values ('Mie Instan');
insert into categories(name) values ('Olahan Daging');

/* Display records */
select categories.id, categories.name as 'category_name', GROUP_CONCAT(products.name) as 'products' from products, categories where products.category_id = categories.id group by categories.id;