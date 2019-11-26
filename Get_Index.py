def Di_rel(X,DIo):
  soma=0
  for j in range(ncol):
    for i in range(nrow):
        Xj=np.mean(X[:,j])
        soma=soma+(X[i,j]-Xj)**2
  DI=(soma/nrow)**0.5
  DIr=DI/DIo
  return DIr


Adjust_F_CR(DIr,Fo,CRo,y_cod_F,y_cod_CR,Fc):

  Fd=DIr
  CRa=np.copy(CRo)
  Fa=np.copy(Fo)

  if(y_cod_F>0):
    Fo=Fo*(1+Fd) #Fo=Fo+Fc
  else:
    Fo=Fo*(1-Fd) 
  Fo=(3*Fo+Fa)/4 # para suavizar
    
  if(y_cod_CR>0):
    CRo=CRo*(1+Fd) 
  else:
    CRo=CRo*(1-Fd) 
  CRo=(3*CRo+CRa)/4 # para suavizar
     
  # reajuste do intervalo (se necessario)
  if(CRo> 1):
    CRo=1
  if(CRo< 0.05):
    CRo=0.05
      
  # reajuste do intervalo (se necessario)
  if(Fo> 1):
    Fo=1
  if(Fo< 0.05):
    Fo=0.05
      
  return Fo,CRo
