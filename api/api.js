export function postGetdraftAction({ $axios }, { body }) {
  return $axios.post('getdraft', body);
}

export function postSaveAction({ $axios }, { body }) {
  return $axios.post('save/', body);
}

export function postCalculatorAction({ $axios }, { body }) {
  return $axios.post('calculator/', body);
}

export function postBuyAction({ $axios }, { body }) {
  return $axios.post('buy/', body);
}
