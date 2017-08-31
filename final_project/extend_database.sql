use Endangered;

drop table if exists Tweet;
create table Tweet (
  tweet_id varchar(32) generated always 
     as (json_unquote(json_extract(tweet_doc, '$.id_str'))) stored primary key,
  screen_name varchar(32) generated always 
     as (json_unquote(json_extract(tweet_doc, '$.user.screen_name'))) stored,
  retweet_count int
     as (json_unquote(json_extract(tweet_doc, '$.retweet_count'))) stored,
  tweet_doc json,
  continent_name varchar(255),
  foreign key (continent_name) references Continent(continent_name)
);
