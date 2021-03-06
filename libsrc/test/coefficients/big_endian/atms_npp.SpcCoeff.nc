CDF       
      
n_Channels           
   write_module_history      O$Id: SpcCoeff_netCDF_IO.f90 13518 2011-04-22 17:25:42Z paul.vandelst@noaa.gov $    creation_date_and_time        2012/02/06, 18:37:54 -0500UTC      Release             Version             	Sensor_Id         atms_npp   WMO_Satellite_Id         �   WMO_Sensor_Id           m   Title         bSpectral coefficients for atms_npp derived from SRF data file atms_npp.osrf.nc and solar data file     History       �$Id: Create_SpcCoeff.f90 17123 2012-01-06 14:42:58Z david.groff@noaa.gov $; $Id: MW_SensorData2oSRF.f90 14745 2011-07-28 17:19:22Z yong.chen@noaa.gov $; $Id: MW_SensorData_Define.f90 17596 2012-02-06 23:13:04Z paul.vandelst@noaa.gov $;    Comment       �; oSRF Information: The SRF for this sensor is computed from central frequencies and intermediate frequencies assuming a boxcar response across the passband-width. Each channel contains 256 points.; Solar Information:            Sensor_Type              	long_name         Sensor Type    description       <Sensor type to identify uW, IR, VIS, UV, etc sensor channels   units         N/A    
_FillValue                    �   Sensor_Channel                  	long_name         Sensor Channel     description       List of sensor channel numbers     units         N/A    
_FillValue                  X  �   Polarization                	long_name         Polarization type flag     description       Polarization type flag.    units         N/A    
_FillValue                  X  �   Channel_Flag                	long_name         Channel flag   description       Bit position flags for channels    units         N/A    
_FillValue                  X  P   	Frequency                   	long_name         	Frequency      description       Channel central frequency, f   units         Gigahertz (GHz)    
_FillValue                      �  �   
Wavenumber                  	long_name         
Wavenumber     description       Channel central wavenumber, v      units         Inverse centimetres (cm^-1)    
_FillValue                      �  X   	Planck_C1                   	long_name         	Planck C1      description        First Planck coefficient, c1.v^3   units         mW/(m^2.sr.cm^-1)      
_FillValue                      �     	Planck_C2                   	long_name         	Planck C2      description       Second Planck coefficient, c2.v    units         
Kelvin (K)     
_FillValue                      �  �   Band_C1                 	long_name         Band C1    description       $Polychromatic band correction offset   units         
Kelvin (K)     
_FillValue                      �  h   Band_C2                 	long_name         Band C2    description       #Polychromatic band correction slope    units         K/K    
_FillValue                      �     Cosmic_Background_Radiance                  	long_name         Cosmic Background Radiance     description       5Planck radiance for the cosmic background temperature      units         mW/(m^2.sr.cm^-1)      
_FillValue                      �  �   Solar_Irradiance                	long_name         Kurucz Solar Irradiance    description       *TOA solar irradiance using Kurucz spectrum     units         mW/(m^2.cm^-1)     
_FillValue                      �  x                              	   
                                       	   	   
   
   
   
   
   
   
   
   
   
   
   
   
   	   
   
   
   
   
   
                                                                                        @7������@?fffffd@I&ffffe@I�G�z�@Jffffff@J�I�^5>@K333333@KxQ��@K������@L�)� K~@L�)� K@L�)� K@L�)� K@L�)� K@L�)� K�@V�����@d�     @f���P@f���R@f���Q@f���R@f���R?�g|^�|�?��V2�b?��a���?��ۑ��k?�-�^f�?���ؠju?��#2״?�RU�k(�?��؊��?��t��M?��t��N?��t��N?��t��N?��t��N?��t��O@�I�L��@�9�i@uP�Ѣ@uP�Ѥ@uP�ѣ@uP�Ѥ@uP�Ѥ>���!y�>�<��%?~��;9�?��y�2?����?�C�	�?������?7cX�W?�[dT�?�#ՙhP?�#ՙhR?�#ՙhR?�#ՙhR?�#ՙhR?�#ՙhT?3��O_c0?`jQ􂬜?fN:�s?fN:�y?fN:�v?fN:�y?fN:�y?�F��m[?���4�\@O����[@�h*H�1@E�w[(@��G�r^@��cp|�@��g(Z@Oe�.@���_��@���_��@���_��@���_��@���_��@���_��@o@�]/��@!�O�d��@!�O�d��@!�O�d��@!�O�d��@!�O�d���1&XH  �����  ���KD  ��Ge/[  ���Y@^  ����4S  ��U���  ��'F��  ��u���  ��Ց��  �L�р �!Tn��� �!��  � �Mɀ � 𒘶� �1�;<t` �:�eZ  ��9�G����	�� �lN�W� �T���� �9���  ?� >�(?� ��?� q�m?� 7�c�?� �:�?� ��!�?� �Wm�?� ��e?� �$�?� 
��?� 4Z97?� !���v?� !S�x?� !2R��?� !+l�{?� ,� ��?� $��� ?� ��V?��9��?���"?� g����?�  �Z>�[&?[>�oBOj�?�᫂�?� DJ�?=��Kb?�ǐgT?9�B'd!?�!@�X?��Ε�?	[�=,�?	[�=,�?	[�=,�?	[�=,�?	[�=,�?	[�=,�?U䅌�P?NLy�?uW�UJ?uW�UE?uW�UJ?uW�UE?uW�UE                                                                                                                                                                                