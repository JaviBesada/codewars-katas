def multiTable(n: Int): String ={
  var i=1
  var tabla=""
  while i<11 do
    if i==10 then
      tabla += s"$i * $n = " + i * n
    else
      tabla += s"$i * $n = " + i * n + "\n"
    i += 1
  return tabla
}
