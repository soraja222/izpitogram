% include('head.tpl')

<h1>Uporabniki</h1>
<div class="row">
    <div class="col-4">
    <h2>Ustvari uporabnika</h2>
    <form action="/uporabniki" method="POST">
        <div class="input-group mb-3">
            <span class="input-group-text">Ime: </span>
            <input type="text" class="form-control" name="ime" placeholder="Ime" aria-label="ime">
            <span class="input-group-text">Priimek: </span>
            <input type="text" class="form-control" name="priimek" placeholder="Priimek" aria-label="priimek">
        </div>
        <div class="input-group mb-3">
        <label class="input-group-text" for="inputGroupSelect01">Smer</label>
        <select class="form-select" name="smer" id="inputGroupSelect01">
            <option selected>Izberi...</option>
            <option value="Financna Matematika">Financna Matematika</option>
            <option value="Splosna Matematika">Splosna Matematika</option>
            <option value="Pedagoska Matematika">Pedagoska Matematika</option>
        </select>
        </div>
        <button type="submit" class="btn btn-primary w-100">Potrdi</button>
    </form>
    </div>
    <div class="col-4">
        % for uporabnik in uporabniki:
            <a href="/uporabniki/{{uporabnik.ime}}_{{uporabnik.priimek}}" class=" m-1 col-12 btn btn-primary">{{uporabnik.ime}} {{uporabnik.priimek}}</a>
        % end
    </div>
    <div class="col-4"></div>
</div>
% include('foot.tpl')