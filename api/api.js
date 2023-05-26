export function postGetdraftAction({ $axios }, { body }) {
  return $axios.post('insurance/getdraft/', body);
}

export function postSaveAction({ $axios }, { body }) {
  return $axios.post('insurance/save/', body);
}

export function postCalculatorAction({ $axios }, { body }) {
  return $axios.post('insurance/calculator/', body);
}

export function postBuyAction({ $axios }, { body }) {
  return $axios.post('insurance/buy/', body);
}
