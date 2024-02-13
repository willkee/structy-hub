def tribonacci(n):  
  store = {}
  
  def _trib(n, store):
    if n < 2: return 0
    if n == 2: return 1
  
    if n in store:
      return store[n]
    
    store[n] = _trib(n - 1, store) + _trib(n - 2, store) + _trib(n - 3, store)
    
    return store[n]
  return _trib(n, store)
    