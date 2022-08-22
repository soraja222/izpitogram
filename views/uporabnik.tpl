% include('head.tpl')

<h1>{{uporabnik.ime}} {{uporabnik.priimek}}</h1>

<h3>Predmeti</h3>
% for predmet in uporabnik.predmeti:
    <li>{{predmet.letnik}}. {{predmet.ime}}<li>
        % for opravilo in predmet.opravila:
            <li>{{opravilo.ime}}. {{opravilo.rok.mesec}}.{{opravilo.rok.dan}} {{opravilo.opravljen}}<li>
        % end
% end
<h3>Opravila</h3>
% for opravilo in predmet.opravila:
    <li>{{opravilo.ime}}. {{opravilo.rok.mesec}}.{{opravilo.rok.dan}} {{opravilo.opravljen}}<li>
% end

% include('foot.tpl')
