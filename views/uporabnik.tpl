% include('head.tpl')

<h1>{{uporabnik.ime}} {{uporabnik.priimek}}</h1>

<div class="row">
<div class="col-3">
<h2>Ustvari predmet</h2>
    <form action="{{predmet_action}}" method="POST">
        <div class="input-group mb-3">
            <span class="input-group-text">Ime: </span>
            <input type="text" class="form-control" name="ime" placeholder="Ime" aria-label="ime">
        </div>
        <div class="input-group mb-3">
        <label class="input-group-text" for="inputGroupSelect01">Letnik</label>
        <select class="form-select" name="letnik" id="inputGroupSelect01">
            <option selected>Izberi...</option>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
        </select>
        </div>
        <button type="submit" class="btn btn-primary w-100">Potrdi</button>
    </form>
</div>
<div class="col-3">
<h3>Predmeti</h3>
<hr>
% for i, predmet in enumerate(uporabnik.predmeti):
    <h4>{{predmet.letnik}}. letnik - {{predmet.ime}}<h4>
        % for j, opravilo in enumerate(predmet.opravila):
            % if not opravilo.opravljen:
                <a class="btn w-75 m-1 btn-{{'danger' if opravilo.nujno() else 'primary'}}"><b>{{opravilo.tip}}:</b> {{opravilo.ime}} {{opravilo.rok.dan}}/{{opravilo.rok.mesec}}/{{opravilo.rok.leto}}</a>
                <a class="btn m-1 w-10 btn-{{'danger' if opravilo.nujno() else 'primary'}}" href="/uporabniki/{{uporabnik.ime}}_{{uporabnik.priimek}}/predmet/{{i}}/opravilo/{{j}}/opravljen">OK</a>
        % end
% end
</div>

<div class="col-3">
    <h3>Opravila</h3>
    <hr>

    <div class="accordion" id="accordionExample">

        <div class="accordion-item">
            % for i, opravilo in enumerate(opravila):
                <a id="heading{{i}}" data-bs-toggle="collapse" data-bs-target="#collapse{{i}}" aria-expanded="false" aria-controls="collapse{{i}}" class="accordion-header btn m-1 w-100 btn-{{'danger' if opravilo.nujno() else 'primary'}}"><b>{{opravilo.tip}}:</b> {{opravilo.ime}} {{opravilo.rok.dan}}/{{opravilo.rok.mesec}}/{{opravilo.rok.leto}}</a>
                    <div id="collapse{{i}}" class="accordion-collapse collapse" aria-labelledby="heading{{i}}" data-bs-parent="#accordionExample">
                        <div class="accordion-body">
                                <p>Začni se učiti: {{opravilo.rok.ucenje()}}</p>
                                <p>Prijavi se v VIS-u: {{opravilo.rok.prijava()}}</p>
                                <p>Rok: {{opravilo.rok.dan}}.{{opravilo.rok.mesec}}.{{opravilo.rok.leto}}</p>
                        </div>
                    </div>
            % end
        </div>
    </div>
</div>



<div class="col-3">
<h2>Ustvari opravilo</h2>
    <form action="{{opravilo_action}}" method="POST">
        <div class="input-group mb-3">
            <span class="input-group-text">Ime: </span>
            <input type="text" class="form-control" name="ime" placeholder="Ime" aria-label="ime">
        </div>

        <div class="input-group mb-3">
            <span class="input-group-text">Leto: </span>
            <input type="text" class="form-control" name="leto" value="{{leto}}" placeholder="{{leto}}" aria-label="leto">
            <span class="input-group-text">Mesec: </span>
            <input type="text" class="form-control" name="mesec" value="{{mesec}}" placeholder="{{mesec}}" aria-label="mesec">
            <span class="input-group-text">Dan: </span>
            <input type="text" class="form-control" name="dan" value="{{dan}}" placeholder="{{dan}}" aria-label="dan">
        </div>

        <div class="input-group mb-3">
        <label class="input-group-text" for="inputGroupSelect01">Tip obveznosti</label>
        <select class="form-select" name="tip_obveznosti" id="inputGroupSelect01">
            <option selected>Izberi...</option>
                <option value="izpit">Izpit</option>
                <option value="ustni_zagovor">Ustni zagovor</option>
                <option value="seminarska_naloga">Seminarska naloga</option>
        </select>
        </div>

        <div class="input-group mb-3">
        <label class="input-group-text" for="inputGroupSelect01">Predmet</label>
        <select class="form-select" name="predmet" id="inputGroupSelect01">
            <option selected>Izberi...</option>
            % for i, predmet in enumerate(predmeti):
                <option value="{{i}}">{{predmet.letnik}}. letnik - {{predmet.ime}}</option>
            % end
        </select>
        </div>
        <button type="submit" class="btn btn-primary w-100">Potrdi</button>
    </form>
</div>

</div>

% include('foot.tpl')
