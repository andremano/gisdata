.. _sec-data-entry:

Data Entry
==========

In this exercise, you will create spatial data from scratch through digitization, a form of data entry. You will learn how to design a data model and ensure topological correctness.
Additionally, the exercise demonstrates a common spatial data workflow: converting tabular data into a spatial format.

Direct Spatial Data Acquisition 
-------------------------------

Spatial data acquisition can be done from several sources. There has been an increase in data acquired (or produced) using Remote sensing such as satellite imagery.

Other sources of spatial data include Aerial survey, Terrestrial survey and Crowdsourcing. The use of different spatial data sources implies that how suitable (strengths and weaknesses) each particular source is for a particular analysis, depends on the acquisition methods. In this section we focus on methods for direct or **primary** data acquisition.

.. attention::
   What are possible the advantages and disadvantage of using the data sources listed in the table below? Fill in at least one advantage and one disadvantage.

    ==================      =========   ============
    Data Source             Advantage   Disadvantage 
    ==================      =========   ============
    Remote sensing          \           \
    Aerial survey [#]_      \           \
    Terrestrial survey      \           \
    Crowdsourcing           \           \
    ==================      =========   ============

    .. [#] It should be noted that aerial surveys are a form of remote sensing, but not from space. 


-----------------------------

Indirect Spatial Data Acquisition 
---------------------------------

Although spatial data can be acquired from third-party sources like government agencies or specialised companies, there will always be the need to acquire your own data. This usually means ‘digitising’ also known as ‘vectorisation’ – the process of capturing objects from a raster base layer like a map or an aerial photograph as points, lines and polygons. In this section, we focus on methods for indirect or **secundary** data acquisition. Specifically, the main techniques used for *vectorisation*. 

.. note::
   **Resources.**
   You will require the latest LTR version of `QGIS <https://qgis.org/download/>`_, plus the dataset `data_entry.zip <_static/datasets/data_entry.zip>`_.  When you unzip the dataset, you will find the following files inside:

   + ``data_entry.qgs`` – a QGIS project file;
   + ``Pearl_Harbour_topographic_map_(1999).tif`` – a raster map; 
   + ``Educational_facilities.csv`` – tabular data; 
   + ``Polygons.gpk`` – a polygon vector layer. 

.. _`sec-digitising`:

Digitising 
^^^^^^^^^^

Extracting the data, you need from a raster base map to a vector layer starts with creating a new dataset (i.e. layer), where the features that are about to be created will be stored. Technically speaking, it is a simple task; however, you should always take a moment to assess the requirements before proceeding with the actual software operation. 

Capturing elements from a base map is an abstraction exercise; this abstraction depends on the scale and purpose for which the data will be used. For example, think of airports; will you represent them (abstract them) as points or as polygons? The answer to this question will depend on how you are going to use the data. If you want to publish a world map of the major airports, probably you could depict them as points. But if you're going to map the accessibilities to a given airport, a larger scale will be needed; therefore, polygons might be better.  

The attributes associated  with the geometries are another important aspect to consider. The choice of attributes depends not only on the scale and intended use, but it also depends on the availability of the data (e.g. what is the capacity of the airport? How does it rank on security? How many international connections does it serve? – would these be information you need to have? And if so, do you have access to this data?)


Task 1
   Start QGIS and open the ``data_entry.qgs`` project. Among others, you will see a layer named ``Pearl_Harbour_topographic_map_(1999).tif`` Observe the map and complete the table below, considering the following requirements: 

   + Think of at least three vector layers that can be acquired from the raster base map;  
   + Make sure all geometric types – Polygon, Line, Point are represented;  
   + For each layer think of at least two attributes. 

   ===========     ===============   ===========     ===========
   LayerName       Geometric Type    Attribute 1     Attribute 2 
   ===========     ===============   ===========     ===========
   water_lines     line                Id              length 
   \               \                   \               \
   \               \                   \               \
   \               \                   \               \
   \               \                   \               \
   \               \                   \               \
   \               \                   \               \
   ===========     ===============   ===========     ===========

Task 2
   Now that you know what you want to extract and how are you are going to abstract it, proceed with the creation of the new layers. Digitise at least three features per layer. 

   For this task, you may want to watch the video tutorial on `basic digitizing <https://player.vimeo.com/external/316725601.hd.mp4?s=c6af68bb5180619816eb0b847933d22d0f2972f2&profile_id=175>`_:

.. raw:: html
    
   <div style="padding:53.75% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/316725601?color=007e83&portrait=0" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

\

.. note:: 
   **QGIS.**
   Refer to `Editing <https://docs.qgis.org/3.40/en/docs/user_manual/working_with_vector/editing_geometry_attributes.html>`_ for a detailed description of vector editing with QGIS.


.. _sec-topology-con:

Topological Consistency 
^^^^^^^^^^^^^^^^^^^^^^^

**Topology** refers to the spatial relationships that should exist among the geometries of a vector dataset. Topology can be a complex subject, but we will take a very pragmatic approach and show you how to maintain the most common topological relationship: adjacency in polygons and connectivity of lines.

.. figure:: _static/figures/data_entry/common-topo-rel.png
   :alt: topological relations
   :figclass: align-center

   Common topological relations on polygons, lines, and points


In the previous task, for the layer of geometry type ‘Line’ you probably digitised something that is supposed to be a network like roads or water lines. The key characteristic of a network is *connectivity*. However, if you happen to have digitised lines that are supposed to be connected and you zoom in to the point where the intersection is supposed to be, you will see that lines are not connected. Instead, you will see connectivity issues either by excess or by insufficiency (also known as *overshoots* and *undershoots* respectively). 


.. figure:: _static/figures/data_entry/under-shoot.png
   :alt: undershoot
   :figclass: align-center

   Connectivity issues between lines. The case of undershooting

To ensure topological consistency between geometries, e.g., that line segments get properly connected while digitising, we have to set a snapping tolerance, which tells the GIS software to connect lines that are within certain distance automatically. Otherwise, it will be impossible to ensure that our lines are connected.


Task 3
   In QGIS, go to :guilabel:`Project` > :guilabel:`Spaning Options` and enable :guilabel:`Snapping mode`. Enter a tolerance of :math:`20 px` for every layer of lines that you may have. 

   If you may want to watch the video tutorial on  `advance editing <https://utwente.yuja.com/V/Video?v=932806&node=5064902&a=124206270>`_ :

.. raw:: html

   <div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://utwente.yuja.com/V/Video?v=932806&node=5064902&a=124206270" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

\

Task 4
   Digitise some new lines making sure they are topologically connected.  You will notice during digitising; if you go closer than a certain distance of an existing feature; the line would be automatically ‘pulled’ towards the nearest vertex or segment of the closest feature. You are thus ensuring connectivity. 

   In the case of polygons, it is also possible to ensure that adjacent polygons do not overlap. 

.. attention:: 
   + How to define a snapping tolerance?
   + What do the options ‘Enable topological editing’ and  ‘Enable snapping on intersection’ allow you to do? Try to think of situations where these options might be useful. 

 
.. _spatialising-data:

Spatialising Data
^^^^^^^^^^^^^^^^^ 

Another way to acquire spatial data is by means of spatialising data. In other words, associate a geographic location with objects. This is a very common procedure when you get, for example, a spreadsheet or some sort of tabular data. 
 
You can spatialise your data in two ways. By means of a *join* (a concept that will be explored later ahead in the course), or by means of building point geometries given that the tabular data contains X and Y coordinates.  


Task 6
   Spatialising data. Open the ``data_entry.qgs`` project and create a point layer using the ``educational_facilities.csv`` file. Follow the steps depicted in the screenshot below.

.. figure:: _static/figures/data_entry/spacialising.png
   :alt: Create new point layer
   :figclass: align-center

   Step to create a point layer from the 'educational_facilities.csv' file


.. attention::
   If all went well, you should have ended up with a layer of points in your project. Does that mean that the ``educational_facilities.csv`` is spatial data?


In the Appendices section, you find a list of :ref:`gis-formats`. 

.. sectionauthor:: André da Silva Mano & Manuel Garcia Alvarez  
