% include('head.tpl')

<h1>Uporabniki</h1>
% for uporabnik in uporabniki:
    <a href="/uporabniki/{{uporabnik.ime}}_{{uporabnik.priimek}}">{{uporabnik.ime}} {{uporabnik.priimek}}</a>
% end

% include('foot.tpl')