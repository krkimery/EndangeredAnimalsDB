use Endangered; select continent_name, count(*) tweet_count from Tweet group by continent_name order by tweet_count desc;

use Endangered; select screen_name, retweet_count from Tweet t inner join Continent c on t.continent_name = c.continent_name;

use Endangered; select screen_name, retweet_count from Tweet t right join Continent c on t.continent_name =  c.continent_name;

use Endangered; select continent_name, count(*) tweet_count from Tweet where continent_name = "North America";

use Endangered; select c.continent_name, t.screen_name from Tweet t right join Continent c on t.continent_name = c.continent_name;