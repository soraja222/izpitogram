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
% for predmet in uporabnik.predmeti:
    <h4>{{predmet.letnik}}. letnik - {{predmet.ime}}<h4>
        % for opravilo in predmet.opravila:
            <a class="btn w-100 m-1 btn-primary">{{opravilo.ime}}. {{opravilo.rok.mesec}}.{{opravilo.rok.dan}} {{opravilo.opravljen}}</a>
        % end
% end
</div>

<div class="col-3">
<h3>Opravila</h3>
<hr>
% for opravilo in opravila:
    <a class="btn m-1 w-100 btn-primary">{{opravilo.ime}}. {{opravilo.rok.mesec}}.{{opravilo.rok.dan}} {{opravilo.opravljen}}</a>
% end
</div>
<div class="col-3">
<h2>Ustvari opravilo</h2>
    <form action="{{opravilo_action}}" method="POST">
        <div class="input-group mb-3">
            <span class="input-group-text">Ime: </span>
            <input type="text" class="form-control" name="ime" placeholder="Ime" aria-label="ime">
        </div>
        <div class="input-group mb-3">
            <span class="input-group-text">Rok: </span>
            <input type="text" class="form-control" name="rok" placeholder="Rok" aria-label="rok">
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
