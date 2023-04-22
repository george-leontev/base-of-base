program Variant13;
var
  s: integer;
  t: integer;
begin
  Readln(s);
  Readln(t);

  if (abs(s) > 3) or (abs(t) > 3) then
  begin
    Writeln ('YES');
  end
  else
  begin
    Writeln('NO');
  end;

end.