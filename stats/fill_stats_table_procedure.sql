create or replace procedure fill_stats_table()
language plpgsql
as $$
declare
  income_ranges cursor for select * from commons_incomerange;
  age_ranges    cursor for select * from commons_agerange;
  categories    cursor for select * from commons_category;
  genderValue   varchar(1) := 'F';
begin
  for income_range in income_ranges loop
    for age_range in age_ranges loop
		for category in categories loop
			for gender in 1..2 loop
				if gender = 1 then
					genderValue := 'F';
					else
					genderValue := 'M';
				end if;
					insert into stats_stat (income_range_id, age_range_id, category_id, gender, value, count)
					values (income_range.id, age_range.id, category.id, genderValue, 0, 0);
			end loop;
		end loop;
  	end loop;
  end loop;
end; $$