/* tslint:disable:variable-name */

export class Stats {
  xp: number;
  xp_required: number;
  lvl: number;
  hp: number;
}

export class Fight {
  monster_id: number;
  monster_hp: number;
}

export class User {
  id: number;
  name: string;
  icon: string;
  current_fight: Fight;
  stats: Stats;
}
