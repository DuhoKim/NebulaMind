const C = 299792.458, HC = 1.2398
export const umToGHz = (um: number) => C / um
export const umToKeV = (um: number) => HC / um / 1000
export const bandUnit = (b: string): 'GHz' | 'keV' | 'μm' =>
  b === 'radio' || b === 'sub_mm' ? 'GHz' : b === 'xray' || b === 'gamma' ? 'keV' : 'μm'
export const convertUm = (um: number, b: string) =>
  b === 'radio' || b === 'sub_mm' ? umToGHz(um) : b === 'xray' || b === 'gamma' ? umToKeV(um) : um
