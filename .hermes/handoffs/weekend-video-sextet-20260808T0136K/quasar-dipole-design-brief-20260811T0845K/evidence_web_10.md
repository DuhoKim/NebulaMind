Exact archive: Resultscode.tar.gz
Verified MD5: cdd8d751b1c160c2c2ad7abf4836d2d4


MEMBER README.md
# CatWISEDipole
Code associated with arXiv:2009.14826 , https://inspirehep.net/literature/1820376

CatWISEAnisotropy.ipynb : Illustrates aspects of selection such as masking.
CatWISE_Dipole_Results.ipynb : Results

Code for Monte Carlo to estimate statistical significance:
runsimulations_CatWISE.py
dipolefunctions_CatWISE.py
helperfunctions.py

Data can be found at : https://doi.org/10.5281/zenodo.4431089

Contact: mrameezphysics@outlook.com for queries


MEMBER runsimulations_CatWISE.py
import numpy as np
import scipy.constants as sc
import sys

import healpy as hp
from astropy.io import fits

from time import time

from dipolefunctions_CatWISE import *
from helperfunctions import *

def main(N,simnum,vel,seed,galcut,direction='CMB') :
	
	print('Running {:0.0f} simulations of initially {:0.0f} sources each for a velocity of {:0.0f} km/s'.format(simnum,N,vel/1000.),flush=True)
	
	catwise_extended = fits.open('../Data/catwise_agns_masked_final_w1lt16p5_alpha.fits')[1].data
	
	flux_w1 = catwise_extended['k']*catwise_extended['nu_W1_iso']**catwise_extended['alpha_W1']
	alpha = -catwise_extended['alpha_W1']
	
	W1_fluxcut = 8.52707e-28
	N_output = len(flux_w1[(flux_w1>W1_fluxcut)])
	dlon,dlat = -121.78,28.80
	
	print('Reading and making mask')
	
	masks = fits.open('../Data/MASKS_exclude_master_final.fits')[1].data
	nside_hi = 1024
	nside_lo = 64
	galcut = 30
	mask = makeMask(masks,galcut=galcut,nside=nside_hi,masking='onesided')
	mask = hp.ud_grade(mask,nside_out=nside_lo)
	mask[(mask!=1)] = 0
	
	print('Beginning simulations')
	
	if direction=='CMB' :
		lonlats_dipole,lonlats_dipole_corrected,d,n = doAll_Vectors_Sim_resampling(N, N_output, simnum, alpha, flux_w1, lon_psmask=[lon_LMC,lon_SMC], lat_psmask=[lat_LMC,lat_SMC], rad_mask=[rad_LMC,rad_SMC], vel=vel, seed=seed, galcut=galcut, do_resampling=True, W1_fluxcut=W1_fluxcut, estimator='healpy', masking='onesided', nside=nside_lo, mask=mask)
	elif direction=='CW' :
		lonlats_dipole,lonlats_dipole_corrected,d,n = doAll_Vectors_Sim_resampling(N, N_output, simnum, alpha, flux_w1, lon_direction=dlon, lat_direction=dlat, lon_psmask=[lon_LMC,lon_SMC], lat_psmask=[lat_LMC,lat_SMC], rad_mask=[rad_LMC,rad_SMC], vel=vel, seed=seed, galcut=galcut, do_resampling=True, W1_fluxcut=W1_fluxcut, estimator='healpy', masking='onesided', nside=nside_lo, mask=mask)
	
	print('Completed.  Writing results to files.',flush=True)
	
	np.savetxt('../SavedData/CatWISE_DipoleSimulations_{:0.0f}sourcesInp_{:0.0f}sourcesOut_{:0.0f}kms_{:0.0f}sims_lonlats_run{:0.0f}_{:s}dir.txt'.format(N,N_output,vel/1000.,simnum,seed,direction),np.array(lonlats_dipole).transpose(),header='Longitude and latitude of uncorrected dipole directions')
	
	np.savetxt('../SavedData/CatWISE_DipoleSimulations_{:0.0f}sourcesInp_{:0.0f}sourcesOut_{:0.0f}kms_{:0.0f}sims_lonlats_corrected_run{:0.0f}_{:s}dir.txt'.format(N,N_output,vel/1000.,simnum,seed,direction),np.array(lonlats_dipole_corrected).transpose(),header='Longitude and latitude of corrected dipole directions')
	
	np.savetxt('../SavedData/CatWISE_DipoleSimulations_{:0.0f}sourcesInp_{:0.0f}sourcesOut_{:0.0f}kms_{:0.0f}sims_d_run{:0.0f}_{:s}dir.txt'.format(N,N_output,vel/1000.,simnum,seed,direction),d,header='Dipole amplitudes (biased)')
	
	np.savetxt('../SavedData/CatWISE_DipoleSimulations_{:0.0f}sourcesInp_{:0.0f}sourcesOut_{:0.0f}kms_{:0.0f}sims_n_run{:0.0f}_{:s}dir.txt'.format(N,N_output,vel/1000.,simnum,seed,direction),n,header='Number of sources of final sample')
	
if __name__ == '__main__' :
	
	if len(sys.argv)<6 :
		raise ValueError('Please provide the five input arguments, N, simnum, vel, seed, and direction.')
	
	N = int(sys.argv[1])
	simnum = int(sys.argv[2])
	vel = float(sys.argv[3])
	seed = int(sys.argv[4])
	galcut = float(sys.argv[5])
	direction = sys.argv[6]
	
	main(N,simnum,vel,seed,galcut,direction=direction)


MEMBER dipolefunctions_CatWISE.py
import numpy as np
import scipy.constants as sc
from lmfit import Minimizer, Parameters
import healpy as hp
#from time import time

lon_CMBdipole = 264.021
lat_CMBdipole = 48.253
velocity_CMBframe = 369000.

lon_LMC,lat_LMC = 280.46526218382076, -32.888503352167234
rad_LMC = 11.5
lon_SMC,lat_SMC = 302.7969909022401, -44.29931060764203
rad_SMC = 5.519999980926514

deg2rad = np.pi / 180.
rad2deg = 180. / np.pi

W1_fluxcut = 1

def dir2vec(lon, lat) :
	
	"""
	Converts longitude and latitude in degrees into a Cartesian vector with unit length
	"""
	
	theta,phi = deg2rad*(90.-lat),deg2rad*lon
	
	ct = np.cos(theta)
	st = np.sin(theta)
	cp = np.cos(phi)
	sp = np.sin(phi)
	
	vec = np.array([st*cp,st*sp,ct])
	
	return vec


def vec2dir(vec) :
	
	"""
	Converts a Cartesian vector with unit length into longitude and latitude in degrees
	"""
	
	x = vec[0]
	y = vec[1]
	z = vec[2]
	
	theta = np.arccos(z)
	phi = np.arctan2(y,x)
	
	lat,lon = 90.-rad2deg*theta,rad2deg*phi
	
	return lon,lat


def angdist(vec1, vec2) :
	
	"""
	Computes the angular distance of two Cartesian vectors with unit length in degrees
	"""
	
	angle = rad2deg * np.arccos(np.dot(vec1,vec2))
	
	return angle


def scattomap(lon, lat, nside=16):
	
	""" Returns a histogram of celestial objects whose position is given in latitute and longitude by bins chosen by HEALPix (at resolution nside) """
	
	hmap = np.zeros(hp.nside2npix(nside))
	hmap = hmap + np.bincount(hp.ang2pix(nside,lon,lat,lonlat=1), minlength=hp.nside2npix(nside))
	
	return hmap


def getRotationMatrix_Z(lon=lon_CMBdipole) :
	
	"""
	Computes the rotation matrix around the Z-axis for moving a vector with longitude lon to the zero meridian
	"""
	
	a1 = -lon
	
	c1 = np.cos(deg2rad * a1)
	s1 = np.sin(deg2rad * a1)
	
	rot_mat = np.array([[c1, -s1, 0],[s1, c1, 0.],[0, 0, 1.]])
	
	return rot_mat


def rotateVectors(vec, rot_mat) :
	
	"""
	Given a rotation matrix, computes the rotated vector of an input Cartesian vector with unit length
	"""
	
	vec_rot = np.matmul(rot_mat,vec)
	
	return vec_rot


def mag2flux(mag, band='W1', fc=0) :
	
	"""
	Converts magnitude in a WISE band to flux in Jy
	
	fc is a correction factor dependent on the measured spectrum
	"""
	
	if band == 'W1' : f0 = 309.54
	elif band == 'W2' : f0 = 171.787
	
	f = f0 * 10**(-mag/2.5)
	
	if fc :
		f/fc
	
	return f


def getDipoleVectors_Crawford(vec) :
	
	
	"""
	Computes the preferred direction and the estimated dipole amplitude from a sample of vectors
	
	This is the linear estimator as employed by Crawford
	"""
	
	num = float(len(vec[0,:]))
	
	dipole = np.sum(vec,axis=1)
	norm = np.sqrt(np.dot(dipole,dipole))
	dipole_norm = dipole/norm
	
	d = 3./num * norm
	
	return dipole_norm,d


def getDipoleVectors_healpy(densitymap, mask=[None], galcut=0, verbose=False) :
	
	
	"""
	Computes the preferred direction and the estimated dipole amplitude from a density map
	
	This is a wrapper for the healpy routine fit_dipole
	"""
	
	if mask[0] != None :
		densitymap[(mask == 0)] = np.nan
	
	residual,monopole,dipole = hp.remove_dipole(densitymap,bad=np.nan,fitval=True,gal_cut=galcut,verbose=verbose)
	norm = np.sqrt(np.dot(dipole,dipole))
	dipole_norm = dipole/norm
	
	d = norm/monopole
	
	return dipole_norm,d


def getDipoleVectors_quadratic(densmap, weights=None, nside=32, mask=[None]):
    
	if mask[0]==None :
		mask = np.ones_like(densmap)
		mask[(densmap==0)]=0
    
	nonzer=[(mask==1)]
	
	def SumToMinimize(pars, outputresiduals=False):
		
		Nbar, A, lon, lat = pars[0], pars[1], pars[2], pars[3]
		pvec = hp.pix2vec(nside, np.arange(hp.nside2npix(nside)))
		vec = dir2vec(lon, lat)
		costhetap = np.cos(angdist(vec, pvec)*deg2rad)
		tos = (np.power( (densmap - Nbar*(1. +  A*costhetap)), 2 )/(Nbar*(1. +  A*costhetap)))
		if outputresiduals :
			return np.sum(tos*nonzer), densmap - Nbar*(1. +  A*costhetap) #1810.04960 Eq 17
		else :
			return np.sum(tos*nonzer)
	
	def lmfittomin(lmpars):
		sppars = list(lmpars.valuesdict().values())
		return SumToMinimize(sppars)
		
	lmp = Parameters()
	
	Nbguess = np.sum(densmap[nonzer])/float(len(densmap[nonzer]))
	initlon,initlat = hp.pix2ang(nside,np.random.choice(np.arange(hp.nside2npix(nside))), lonlat=True)
	inguess = np.array([Nbguess, 0.011, initlon, initlat])
	
	pnames = ['Nbar', 'A', 'DipLon', 'DipLat']
	bnds = ((Nbguess*0.7, Nbguess*1.5),(0, 1.0), (0,360.),(-90.0,90.0))
	
	for val, name, bnd in zip(inguess, pnames, bnds):
		lmp.add(name, value=val, min=bnd[0], max=bnd[1])
	
	minner = Minimizer(lmfittomin, lmp)
	resquad = minner.minimize(method = 'ampgo')
	
	mfval, residualmap = SumToMinimize([resquad.params['Nbar'].value, resquad.params['A'].value, resquad.params['DipLon'].value, resquad.params['DipLat'].value],outputresiduals=True)
	
	vec_dipole = dir2vec(resquad.params['DipLon'].value,resquad.params['DipLat'].value)
	d = resquad.params['A'].value
	
	return vec_dipole,d



def dip2vel(d, x=1., alpha=0.75) :
	
	"""
	Converts dipole amplitude to velocity beta according to Ellis+Baldwin
	"""
	
	vel = d * sc.c / (2.+x*(1.+alpha))
	
	return vel

def vel2dip(vel, x=1., alpha=0.75) :
	
	"""
	Converts velocity to dipole amplitude according to Ellis+Baldwin
	"""
	
	d = vel / sc.c * (2.+x*(1.+alpha))
	
	return d


def correctDirection(dipole_norm, galcut=30.) :
	
	"""
	Corrects the bias in an estimate of dipole direction of a sample of vectors in case the Galactic plane is masked
	
	The calculation of the bias B follows Rubart with small modifications.  His expression of B is
	
		B = (1-1.5*np.cos(alpha)+0.5*np.cos(alpha)**3) / (1-np.cos(alpha)**3)
	
	The two expressions are equivalent.
	"""
	
	lon,lat = vec2dir(dipole_norm)
	rotmat = getRotationMatrix_Z(lon)
	rotmat_inv = np.linalg.inv(rotmat)
	
	
	dipole_norm_rot = np.matmul(rotmat,dipole_norm)
	lon_rot,lat_rot = vec2dir(dipole_norm_rot)
	
	alpha = 90. - galcut
	alpha = deg2rad * alpha
	
	if lat_rot > 0 :
		theta = 90. - lat_rot
	else :
		theta = 90. + lat_rot
	
	theta = deg2rad * theta
	
	
	B = (1.-1./8.*(9.*np.cos(alpha)-np.cos(3*alpha))) / (1.-np.cos(alpha)**3)
	
	theta_cor = np.arctan(np.tan(theta)/B)
	theta_cor = rad2deg * theta_cor
	
	
	if lat_rot > 0 :
		lat_rot_cor = 90. - theta_cor
	else :
		lat_rot_cor = theta_cor - 90.
	
	dipole_norm_rot_cor = dir2vec(lon_rot,lat_rot_cor)
	
	
	dipole_norm_cor = np.matmul(rotmat_inv,dipole_norm_rot_cor)
	
	return dipole_norm_cor





def timeit(function, *args, **kwargs) :
	
	"""
	This function will be used as decorator to time the duration of a function
	"""
	
	def timed(*args,**kwargs) :
		t1 = time()
		result = function(*args,**kwargs)
		t2 = time()

		print('This took {:0.4f} seconds'.format(t2-t1),flush=True)
		
		return result
	
	return timed


def getIsotropicDistributionVectors(N = 1000, seed=123) :
	
	"""
	Returns a sample of N vectors drawn from an isotropic distribution
	"""
	
	N = int(N)
	
	np.random.seed(seed)

	num1 = np.random.randn(N)
	num2 = np.random.randn(N)
	num3 = np.random.randn(N)

	norm = np.sqrt(num1**2+num2**2+num3**2)

	x = num1/norm
	y = num2/norm
	z = num3/norm
	
	vectors = np.vstack((x,y,z))
	
	return vectors


def maskVectors(vec, rot_mat_list, rot_mat_inv_list, angles, galcut=30.,masking='symmetric') :
	
	"""
	This is a weird function.  It applies a mask made up of a Galactic plane mask and point source masks to a sample of vectors.
	
	The rotation matrices move those vectors which are at the center of the point source masks to the North pole.
	They are defined via getRotationMatrix_Mask.
	"""
	
	if galcut :
		
		z = vec[2,:]
		
		notmasked = np.where(np.abs(z) > np.sin(galcut * deg2rad))[0]
		vec = vec[:,notmasked]
	
	for i in range(len(angles)) :
		
		vec_rot = rotateVectors(vec, rot_mat_list[i])
		
		z = vec_rot[2,:]
		
		if masking == 'symmetric' :
			notmasked = np.where(np.abs(z) < np.cos(angles[i] * deg2rad))[0]
		elif masking == 'onesided' :
			notmasked = np.where(z < np.cos(angles[i] * deg2rad))[0]
		vec_rot = vec_rot[:,notmasked]
		
		vec = rotateVectors(vec_rot, rot_mat_inv_list[i])
	
	return vec


def getRotationMatrix_Mask(lon_list, lat_list) :
	
	"""
	Returns a list of rotation matrices and their inverse, each of which rotates vectors pointing
	towards (lonlist,latlist) to the North Galactic pole
	"""
	
	rot_mat_list = []
	rot_mat_inv_list = []
	for i in range(len(lon_list)) :
		
		rot_mat_list.append(getRotationMatrix(lon_list[i],lat_list[i]))
		rot_mat_inv_list.append(np.linalg.inv(rot_mat_list[i]))
	
	return rot_mat_list,rot_mat_inv_list


def aberrateVectors(vec, rot_mat, rot_mat_inv, vel=velocity_CMBframe) :
	
	"""
	Aberrates a sample of vectors according to a specific speed.  
	
	The direction of the velocity is part of the rotation matrix and its invers.
	
	Returns also the angular distance theta of each vector from the velocity direction.
	"""
	
	vec_rot = rotateVectors(vec, rot_mat)
	
	theta = np.arccos(vec_rot[2])
	theta *= rad2deg
	
	beta = vel / sc.c

	ct = vec_rot[2]
	st = np.sqrt(1-ct**2)
	
	theta_aberrated = np.arctan2(st*np.sqrt(1-beta**2), beta+ct)

	vec_rot[2] = np.cos(theta_aberrated)
	
	st_prime = np.sin(theta_aberrated)
	
	vec_rot[:2] *= st_prime/st
	
	vec = rotateVectors(vec_rot, rot_mat_inv)
	
	return vec,theta


def getRotationMatrix(lon=lon_CMBdipole, lat=lat_CMBdipole) :
	
	a1 = -lon
	a1 *= deg2rad
	a2 = lat-90.
	a2 *= deg2rad
	
	c1 = np.cos(a1)
	s1 = np.sin(a1)
	
	c2 = np.cos(a2)
	s2 = np.sin(a2)
	
	rot_mat = np.array([[c2*c1, -c2*s1, s2], [s1, c1, 0.], [-s2*c1, s2*s1, c2]])
	
	return rot_mat


def resampleValues(N,values,seed=123) :
	
	"""
	Returns a sample of size N drawn from the list 'values' with replacement
	"""
	
	N = int(N)
	
	np.random.seed(seed)
	sample = np.random.choice(values,size=N,replace=True)
	
	return sample


def modulateFluxes(theta, flux, alpha, vel=velocity_CMBframe) :
	
	"""
	Modulates flux values according to a velocity using the angular distance theta of each vector from the velocity direction"""
	
	theta *= deg2rad
	
	beta = vel / sc.c
	gamma = 1./np.sqrt(1-beta**2)
	
	factor = (gamma * (1+beta*np.cos(theta)))**(1+alpha)
	
	flux_mod = flux * factor
	
	return flux_mod


def cutSampleVectors(vec, flux, flux_cut) :
	
	"""
	Removes vectors whose flux falls below the flux limit
	"""
	
	indices_cut = np.where(flux > flux_cut)[0]
	
	flux_cut = flux[indices_cut]
	
	vec_cut = vec[:,indices_cut]
	
	return vec_cut,flux_cut

def sampleFlux(N,flux_amp,x,seed=123) :
    
    N = int(N)
    
    np.random.seed(seed)
    sample = np.random.uniform(size=N)
    
    flux_sample = flux_amp * (1-sample)**(-1./x)
    
    return flux_sample

def doAll_Vectors_resampling(N, N_output, rot_mat, rot_mat_inv, rot_mat_mask, rot_mat_mask_inv, maskangles, alpha, flux, x=1., galcut=30., seed=123, vel=velocity_CMBframe, do_resampling=True,W1_fluxcut=W1_fluxcut, add_isotropic=0.,estimator='linear',nside=32,masking='symmetric', mask=[None], weights=[None]) :
	
	"""
	Computes the preferred direction of a simulated sample, as well as its corrected direction, and uncorrected amplitude.
	
	Could perhaps be made a bit smarter...
	"""
	
	vec = getIsotropicDistributionVectors(N=N, seed=seed)
	vec,_ = aberrateVectors(vec, rot_mat, rot_mat_inv, vel=vel)
	vec = maskVectors(vec, rot_mat_mask, rot_mat_mask_inv, maskangles, galcut=galcut, masking=masking)
	
	vec_rot = rotateVectors(vec, rot_mat)
	theta = np.arccos(vec_rot[2]) * rad2deg
	
	N = len(vec[0,:])
	
	if do_resampling :
		flux_sample = resampleValues(N,flux,seed=seed)
		alpha_sample = resampleValues(N,alpha,seed=seed)
	else :
		flux_sample = sampleFlux(N,0.8*W1_fluxcut,x,seed=seed)
		alpha_sample = np.ones(N)*np.mean(alpha)
	
	flux_sample_mod = modulateFluxes(theta, flux_sample, alpha_sample, vel=vel)
	
	vec,_ = cutSampleVectors(vec, flux_sample_mod, W1_fluxcut)
	length = np.shape(vec)[1]
	
	if length >= N_output :
		vec = vec[:,:N_output]
	else :
		print('Vector only has length ',length,'. Pick a larger N')
		return None,None,None,None,None
	
	if add_isotropic :
		N_iso = int(add_isotropic*N_output)
		vec[:,N_output-N_iso:] = getIsotropicDistributionVectors(N=N_iso, seed=seed+123)
	
	
	length = np.shape(vec)[1]
	
	if estimator=='linear' :
		vec_dipole, d = getDipoleVectors_Crawford(vec)
		vec_dipole_corrected = correctDirection(vec_dipole,galcut=galcut)
	
		return vec,vec_dipole,vec_dipole_corrected,d,length
	
	elif estimator=='quadratic' :
		densitymap = scattomap(*vec2dir(vec),nside=nside)
		if weights[0]!=None:
			densitymap*=weights
		vec_dipole, d = getDipoleVectors_quadratic(densitymap,nside=nside,mask=mask)
		
		return vec,vec_dipole,None,d,None
	
	elif estimator=='healpy' :
		densitymap = scattomap(*vec2dir(vec),nside=nside)
		vec_dipole, d = getDipoleVectors_healpy(densitymap,mask=mask,galcut=galcut)
		return vec_dipole,None,d,None


#@timeit
def doAll_Vectors_Sim_resampling(N, N_output, simnum, alpha, flux, x=1., lon_psmask=[lon_LMC,lon_SMC], lat_psmask=[lat_LMC,lat_SMC], rad_mask=[rad_LMC,rad_SMC], seed=123, lon_direction=lon_CMBdipole, lat_direction=lat_CMBdipole, vel=velocity_CMBframe, galcut=30., do_resampling=True,W1_fluxcut=W1_fluxcut, add_isotropic=0.,estimator='linear',nside=32,masking='symmetric', mask=[None], weights=[None]) :
	
	"""
	Same as 'doAll_Vectors_Sim_resampling' but run 'simnum' times
	
	Returns longitudes and latitudes of dipole directions (uncorrected and corrected), 
	as well as dipole amplitudes (uncorrected),
	and number of remaining sources,
	for each simulation
	"""
	
	vecs_dipole = np.zeros((3,simnum))
	vecs_dipole_corrected = np.zeros((3,simnum))
	d = np.zeros(simnum)
	N_remaining = np.zeros(simnum)
	
	rot_mat = getRotationMatrix(lon=lon_direction,lat=lat_direction)
	rot_mat_inv = np.linalg.inv(rot_mat)
	
	rot_mat_mask, rot_mat_mask_inv = getRotationMatrix_Mask(lon_psmask,lat_psmask)
	
	np.random.seed(seed)
	seeds = np.random.rand(simnum)*1e9
	
	for i in range(simnum) :
		vecs_dipole[:,i], vecs_dipole_corrected[:,i], d[i], N_remaining[i] = doAll_Vectors_resampling(N, N_output, rot_mat, rot_mat_inv, rot_mat_mask, rot_mat_mask_inv, rad_mask, alpha, flux, x=x, seed=int(seeds[i]), vel=vel, galcut=galcut, do_resampling=do_resampling,W1_fluxcut=W1_fluxcut, add_isotropic=add_isotropic,estimator=estimator,nside=nside,masking=masking,mask=mask,weights=weights)
		print(str(i+1)+'/'+str(simnum),end='\r')
	
	lonlats = vec2dir(vecs_dipole)
	lonlats_corrected = vec2dir(vecs_dipole_corrected)
	
	
	return lonlats,lonlats_corrected,d,N_remaining




NOTEBOOK CELL 6 code
catwiseAGNs_extended = fits.open('../Data/catwise_agns_masked_final_w1lt16p5_alpha.fits')[1].data

flux_w1_extended, alpha_w1_extended = getFluxAndAlpha(catwiseAGNs_extended)

NOTEBOOK CELL 7 markdown
`catwiseAGNs_extended` is a sample of the complete CatWISE2020 catalog, where cuts were performed as described in the publication, except for the flux cut that is chosen a bit weaker here, $W1<16.5$ instead of $W1<16.4$ (hence `_extended`).  We perform the final cut in the next cell.

NOTEBOOK CELL 8 code
W1_fluxcut = 8.52707e-28 # corresponds to W1<16.4

selected = (flux_w1_extended>W1_fluxcut)
catwiseAGNs = catwiseAGNs_extended[selected]

flux_w1, alpha_w1 = getFluxAndAlpha(catwiseAGNs)

print('The maximum magnitude in the W1 band is {:0.4f}'.format(np.max(catwiseAGNs['w1'])))

NOTEBOOK CELL 13 markdown
# Load masks

NOTEBOOK CELL 14 markdown
Even though the sample is already masked, we here load the masks to perform one more correction to the data.

NOTEBOOK CELL 15 code
masks = fits.open('../Data/MASKS_exclude_master_final.fits')[1].data

NOTEBOOK CELL 16 code
def make_galmask(nside=256, planecut=30) :
    
    """
    Computes a Galactic plane mask
    """
    
    mask = np.ones(hp.nside2npix(nside))
    vector = hp.ang2vec(0,90,lonlat=1)
    indices = hp.query_disc(nside,vector,np.deg2rad(90+planecut))
    mask[indices] = 0
    indices = hp.query_disc(nside,vector,np.deg2rad(90-planecut))
    mask[indices] = 1
    
    return mask

def make_eclmask(nside=256, planecut=30) :
    
    """
    Computes a Galactic plane mask in Ecliptic coordinates
    """
    
    mask = np.ones(hp.nside2npix(nside))
    lon,lat = 0,90
    ra,dec = GalactictoEquatorial(lon,lat)
    C = SkyCoord(ra*u.deg, dec*u.deg, frame='icrs')
    E = C.transform_to('barycentricmeanecliptic')
    lonecl,latecl = E.lon.value,E.lat.value
    vector = hp.ang2vec(lonecl,latecl,lonlat=True)
    indices = hp.query_disc(nside,vector,np.deg2rad(90+planecut))
    mask[indices] = 0
    indices = hp.query_disc(nside,vector,np.deg2rad(90-planecut))
    mask[indices] = 1
    
    return mask

def make_supergalmask(nside=256, planecut=10) :
    
    """
    Computes a Supergalactic plane mask
    """
    
    mask = np.ones(hp.nside2npix(nside))
    slon,slat = 0,90
    S = SkyCoord(slon*u.deg, slat*u.deg, frame='supergalactic')
    G = S.transform_to('galactic')
    lon,lat = G.l.value,G.b.value
    vector = hp.ang2vec(lon,lat,lonlat=True)
    indices = hp.query_disc(nside,vector,np.deg2rad(90+planecut))
    mask[indices] = 0
    indices = hp.query_disc(nside,vector,np.deg2rad(90-planecut))
    mask[indices] = 1
    
    return mask

def makeMask(psmasks,nside=256,galcut=0,masking='symmetric',ecliptic=False,nops=False,factor=1.) :
    
    """
    Computes a mask given a file that specifies locations and extent of point sources
    """
    
    mask = np.ones(hp.nside2npix(nside))
    pixels = np.arange(hp.nside2npix(nside))
    mask_lon,mask_lat = hp.pix2ang(nside,pixels,lonlat=True)

    cmasks = psmasks[(psmasks['pa']<=2)*(psmasks['radius']<15)]
    emasks = psmasks[(psmasks['pa']>2)]
    
    if nops :
        cmasks = psmasks[(psmasks['pa']<=2)*(psmasks['radius']>5)]
        emasks = psmasks[(psmasks['pa']>2)*(psmasks['radius']>5)]
        
    cmask_lon,cmask_lat,cmask_rad = *EquatorialtoGalactic(cmasks['ra'],cmasks['dec']),cmasks['radius']
    
    if ecliptic :
        Cmask = SkyCoord(cmasks['ra']*u.deg, cmasks['dec']*u.deg, frame='icrs')
        Emask = Cmask.transform_to('barycentricmeanecliptic')
        cmask_lon,cmask_lat = Emask.lon.value,Emask.lat.value
    
    for lon,lat,radius in zip(cmask_lon,cmask_lat,cmask_rad):
        vector = hp.ang2vec(lon,lat,lonlat=True)
        indices = hp.query_disc(nside,vector,factor*np.deg2rad(radius))
        mask[indices] = 0
        if masking=='symmetric' :
            indices = hp.query_disc(nside,-vector,factor*np.deg2rad(radius))
            mask[indices] = 0
    
    emask_lon,emask_lat,emask_rad,emask_ba,emask_pa = *EquatorialtoGalactic(emasks['ra'],emasks['dec']),emasks['radius'], emasks['ba'], emasks['pa']
    
    if ecliptic :
        Cmask = SkyCoord(emasks['ra']*u.deg, emasks['dec']*u.deg, frame='icrs')
        Emask = Cmask.transform_to('barycentricmeanecliptic')
        emask_lon,emask_lat = Emask.lon.value,Emask.lat.value

    for lon,lat,rad,ba,pa in zip(emask_lon,emask_lat,emask_rad,emask_ba,emask_pa) :
        ell = evaluateEllipse(mask_lon,mask_lat,lon,lat,factor*rad,ba,pa)
        mask[ell] = 0
        if masking=='symmetric' :
            ell = evaluateEllipse(mask_lon,mask_lat,lon+180.,-1.*lat,factor*rad,ba,-1.*pa)
            mask[ell] = 0
    
    if galcut : 
        planemask = make_galmask(nside=nside,planecut=galcut)
        if ecliptic :
            planemask = make_eclmask(nside=nside,planecut=galcut)
    else : planemask = np.ones_like(mask)
    
    return mask*planemask

NOTEBOOK CELL 17 markdown
Make a high-resolution and a low-resolution mask (a downgraded version of the high-resolution mask, were all pixels that are not 1 after downgrading are set to 0).

NOTEBOOK CELL 18 code
nside_hi = 1024
nside_lo = 64

hires_mask = makeMask(masks,galcut=30,nside=nside_hi,masking='onesided',factor=1)
lores_mask = hp.ud_grade(hires_mask,nside_out=nside_lo)
lores_mask = lores_mask.copy()
lores_mask[(lores_mask!=1)]=0

NOTEBOOK CELL 20 markdown
Make an ecliptic-coordinates version of the high-resolution mask

NOTEBOOK CELL 21 code
hires_mask_ecl = makeMask(masks,galcut=30,nside=nside_hi,masking='onesided',ecliptic=True)

NOTEBOOK CELL 23 markdown
# Check for ecliptic bias

NOTEBOOK CELL 24 markdown
First transform coordinates of the sources to ecliptic coordinates

NOTEBOOK CELL 25 code
ra,dec = GalactictoEquatorial(lon,lat)
C = SkyCoord(ra*u.deg, dec*u.deg, frame='icrs')
E = C.transform_to('barycentricmeanecliptic')
ecl_lon,ecl_lat = E.lon.value,E.lat.value

NOTEBOOK CELL 26 markdown
Now count how many sources are in bins of constant ecliptic latitude (`1` for positive, and `2` for negative latitudes)...

NOTEBOOK CELL 27 code
latmap = hp.pix2ang(nside_hi,np.arange(hp.nside2npix(nside_hi)),lonlat=True)[1]

nbins=20

binedges1 = np.linspace(0,90,num=nbins+1)
binedges2 = np.linspace(-90,-0,num=nbins+1)
bincenters1 = binedges1[:-1]+np.diff(binedges1)[0]/2.
bincenters2 = binedges2[:-1]+np.diff(binedges2)[0]/2.
unmasked1 = np.zeros(nbins)
unmasked2 = np.zeros(nbins)
num1 = np.zeros(nbins)
num2 = np.zeros(nbins)

for i in range(nbins) :
    unmasked1[i] = np.sum(hires_mask_ecl[(latmap>binedges1[i])*(latmap<binedges1[i+1])])
    unmasked2[i] = np.sum(hires_mask_ecl[(latmap>binedges2[i])*(latmap<binedges2[i+1])])
    num1[i] = len(ecl_lat[(ecl_lat>binedges1[i])*(ecl_lat<binedges1[i+1])])
    num2[i] = len(ecl_lat[(ecl_lat>binedges2[i])*(ecl_lat<binedges2[i+1])])

NOTEBOOK CELL 29 code
bincenters = np.hstack((bincenters1,bincenters2))
unmasked = np.hstack((unmasked1,unmasked2))
num = np.hstack((num1,num2))

select = (unmasked!=0)

bincenters = bincenters[select]
unmasked = unmasked[select]
num = num[select]

NOTEBOOK CELL 31 code
pfit = np.polyfit(np.abs(bincenters),num/unmasked,1,w=1/(1/np.sqrt(num))**1)

print('slope = {:0.4f} 1/deg3'.format(pfit[0]*(60./hp.nside2resol(nside_hi,arcmin=True))**2))
print('offset = {:0.4f} 1/deg2'.format(pfit[1]*(60./hp.nside2resol(nside_hi,arcmin=True))**2))

NOTEBOOK CELL 32 code
plt.figure(figsize=(9,5),facecolor='w')

plt.errorbar(bincenters,num/unmasked*(60./hp.nside2resol(nside_hi, arcmin = True))**2,yerr=1/np.sqrt(num) * (60./hp.nside2resol(nside_hi, arcmin = True))**2,marker='o',lw=0,elinewidth=1)

elats = np.linspace(-90,90,num=100)
plt.plot(elats,pfit[1]*(60./hp.nside2resol(nside_hi,arcmin=True))**2+pfit[0]*(60./hp.nside2resol(nside_hi,arcmin=True))**2*np.abs(elats),color='gray',lw=2)

plt.text(-60,70.5,'{:.4}-{:.2}'.format(pfit[1]*(60./hp.nside2resol(nside_hi,arcmin=True))**2,-pfit[0]*(60./hp.nside2resol(nside_hi,arcmin=True))**2)+r'$\cdot |b_{ecl}|$',horizontalalignment='left')

plt.grid()

plt.xlabel('Ecliptic latitude')
plt.ylabel(r'\# sources per deg$^2$')

plt.xlim(-90,90)
plt.ylim(59,76);

NOTEBOOK CELL 33 markdown
# Correct for ecliptic bias

NOTEBOOK CELL 34 markdown
We correct for the ecliptic bias by up-weighing the source density in those pixels that are closer to the ecliptic poles, to match the source density at the ecliptic equator.

NOTEBOOK CELL 35 code
pixels = np.arange(hp.nside2npix(nside_lo))
plon,plat = hp.pix2ang(nside_lo, pixels, lonlat=True)
gc = SkyCoord(plon * u.deg, plat * u.deg, frame='galactic')
ec = gc.barycentricmeanecliptic
elat = ec.lat.degree

densitymap_eclcor = densitymap*(60./hp.nside2resol(nside_lo,arcmin=True))**2 - pfit[0]*(60./hp.nside2resol(nside_hi,arcmin=True))**2*np.abs(elat)

NOTEBOOK CELL 40 code
densitymap_eclcor_smoothed = np.zeros_like(densitymap_eclcor)
zero = np.where(lores_mask==0)[0]
nonzero = np.where(lores_mask==1)[0]
densitymap_eclcor[zero] = np.nan
smoothingradius = np.rad2deg(omega_to_theta(1.).value)

for n,i in enumerate(nonzero) :
    vec = hp.pix2vec(nside_lo,i)
    disc = hp.query_disc(nside_lo,vec,np.deg2rad(smoothingradius))
    densitymap_eclcor_smoothed[i] = np.nanmean(densitymap_eclcor[disc])

densitymap_eclcor_smoothed[(lores_mask==0)]=np.nan

NOTEBOOK CELL 43 code
hp.write_map('../Data/CatWISE_EclCor_Map_nside64.fits',densitymap_eclcor)
hp.write_map('../Data/CatWISE_Mask_nside64.fits',lores_mask)

NOTEBOOK CELL 46 code
dvec,d = getDipoleVectors_healpy(densitymap_eclcor,mask=lores_mask)
dlon,dlat = vec2dir(dvec)

cat_angdist = angdist(dvec,dir2vec(lon_CMBdipole,lat_CMBdipole))

print('We find the dipole amplitude D={:0.5f} in direction (lon,lat)=({:0.2f},{:0.2f})deg'.format(d,*vec2dir(dvec)))
print('This is {:0.2f}deg away from the CMB dipole direction, and roughly corresponds to a velocity of v={:0.2f}km/s'.format(cat_angdist,dip2vel(d,alpha=np.mean(alpha_w1),x=1.7)/1000.))

NOTEBOOK CELL 47 markdown
The estimate of the dipole velocity is based on the mean value of the spectral indices $\alpha$ and the value of the integrated flux density index $x$ close to the flux density cut, which we measure to be ~1.7.

NOTEBOOK CELL 51 code
W1_fluxcut = 8.52707e-28         # Corresponds to a magnitude of W1<16.4

input_velocity = 369.82*1000     # Input velocity in m/s

N_input = 3.3e6                  # How many sources to begin with
N_output = len(catwiseAGNs)      # How many sources to end up with, after all cuts (as many as the sample has)
N_sim = 30                       # Number of simulations

random_seed = 5000               # Must be an integer, from this an array of random seeds is defined within the loop, 
                                 # such that each simulation is based on a different seed

lonlats_sim_hp = np.zeros((2,N_sim))
lonlats_cor_sim_hp = np.zeros((2,N_sim))
d_sim_hp = np.zeros(N_sim)
N_remaining_sim_hp = np.zeros(N_sim)

t1 = time()

lonlats_sim_hp,_,d_sim_hp,N_remaining_sim_hp = doAll_Vectors_Sim_resampling(N_input,
                                                                                    N_output,
                                                                                    N_sim,
                                                                                    alpha_w1_extended,
                                                                                    flux_w1_extended,
                                                                                    lon_psmask=[lon_LMC,lon_SMC],
                                                                                    lat_psmask=[lat_LMC,lat_SMC],
                                                                                    rad_mask=[rad_LMC,rad_SMC],
                                                                                    galcut=30.,
                                                                                    seed=random_seed,
                                                                                    vel=input_velocity,
                                                                                    do_resampling=True,
                                                                                    estimator='healpy',
                                                                                    masking='onesided',
                                                                                    nside=nside_lo,
                                                                                    W1_fluxcut=W1_fluxcut,
                                                                                    mask=lores_mask)

print('This took ',time()-t1,'seconds')

NOTEBOOK CELL 52 code
redselect = '#db2c09'
blueselect = '#1f77b4'
blueselect2 = '#144e78'

plt.figure(facecolor='w',figsize=(8,4))

plt.hist(1000*d_sim_hp,bins=10,alpha=1,color=blueselect,normed=True);

plt.axvline(1000*d,color=redselect)
plt.text(1000*d+0.15,.36,r'CatWISE',rotation=90,fontsize=14,color=redselect,horizontalalignment='left',verticalalignment='top')

plt.axvline(1000*np.median(d_sim_hp),color=blueselect2,lw=0.75,ls='--')
plt.text(1000*np.median(d_sim_hp)+0.15,.36,'CMB',rotation=90,fontsize=14,color=blueselect2,verticalalignment='top')

plt.ylim(0,.37)
plt.xlim(3.5,16.5)
plt.ylabel(r'PDF')
plt.xlabel(r'$\mathcal{D}\;[10^{-3}]$')

plt.tight_layout()