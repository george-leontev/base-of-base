program Variant12_15;

var
  k: integer;
  n: integer;
  max := -30001;

begin
  Readln(k);
  for var x := 0 to k - 1 do
  begin
    Readln(n);  
    if (n < 150) and (n > max) then
    begin
      max := n
    end;
  end;
  Writeln('max = ', max);
end.