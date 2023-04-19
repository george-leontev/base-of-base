program Variant13;
var
  s: integer;
  t: integer;
begin
  readln(s);
  readln(t);
  
  if (abs(s) > 3) or (abs(t) > 3) then 
  begin
    writeln ('YES');
  end
  else
  begin
    writeln('NO');
  end;
  
end.