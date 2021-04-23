export const state = () => ({
  _fullName: 'Cristian Laguna',
  _counter: 0
})

export const getters = {
  getName(state){
    return state._fullName
  },
  getCounter(state){
    return state._counter
  }
}

export const mutations = {
  addCounter(state){
    state._counter++
  }
}