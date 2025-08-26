   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/ol/ol.css">

   <style>
     /* Basic page styling */
     body, html {
       margin: 0;
       padding: 0;
       font-family: Arial, sans-serif;
     }
     #map {
       width: 100%;
       height: 500px; /* fixed height so map is visible */
     }
     #control-panel {
       display: flex;
       flex-direction: column;
       background: white;
       padding: 10px;
       border-radius: 5px;
       box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
       margin-top: 10px;
       max-width: 800px;
     }
     #layer-and-feature-info {
       display: flex;
       flex-direction: row;
       gap: 10px;
       margin-top: 10px;
     }
     #layer-list,
     #feature-info {
       flex: 1;
       padding: 10px;
       border: 1px solid #ddd;
       border-radius: 5px;
       background: #f9f9f9;
       max-height: 300px;
       overflow-y: auto;
     }
     .layer-item {
       display: flex;
       align-items: center;
       margin: 5px 0;
     }
     .layer-item input {
       margin-right: 8px;
     }
     button {
       padding: 5px 10px;
       margin: 5px 0;
       cursor: pointer;
     }
     select, input[type="text"] {
       width: 100%;
       padding: 5px;
       margin: 5px 0;
       box-sizing: border-box;
     }
   </style>

   <div id="map"></div>
   <div id="control-panel">
     <h3>WMS Layer Loader</h3>
     <select id="service-type">
       <option value="wms">WMS</option>
     </select>
     <input type="text" id="service-url" placeholder="Enter WMS service URL">
     <button id="load-service">Load Service</button>
     <div id="layer-and-feature-info">
       <div id="layer-list">
         <p>No layers loaded yet. Enter a service URL and click "Load Service".</p>
       </div>
       <div id="feature-info">
         <p>Click on the map to view feature information.</p>
       </div>
     </div>
   </div>

   <script src="https://cdn.jsdelivr.net/npm/ol@latest/dist/ol.js"></script>

   <script>
     document.addEventListener('DOMContentLoaded', function() {
       const map = new ol.Map({
         target: 'map',
         layers: [
           new ol.layer.Tile({
             source: new ol.source.OSM()
           })
         ],
         view: new ol.View({
           center: ol.proj.fromLonLat([0, 0]),
           zoom: 2
         })
       });

       const loadedServices = {};

       const serviceTypeSelect = document.getElementById('service-type');
       const serviceUrlInput = document.getElementById('service-url');
       const loadServiceButton = document.getElementById('load-service');
       const layerListDiv = document.getElementById('layer-list');
       const featureInfoDiv = document.getElementById('feature-info');

       async function loadService() {
         const serviceUrl = serviceUrlInput.value.trim();
         const serviceType = serviceTypeSelect.value;

         if (!serviceUrl) {
           alert('Please enter a service URL');
           return;
         }

         try {
           if (serviceType === 'wms') {
             await loadWmsService(serviceUrl);
           }
         } catch (error) {
           console.error('Error loading service:', error);
           alert('Failed to load service. Check console for details.');
         }
       }

       async function loadWmsService(serviceUrl) {
         const baseUrl = serviceUrl.split('?')[0];

         if (loadedServices[baseUrl]) {
           updateLayerList();
           return;
         }

         const source = new ol.source.TileWMS({
           url: baseUrl,
           params: { 'LAYERS': '', 'TILED': true },
           serverType: 'geoserver',
           crossOrigin: 'anonymous'
         });

         const parser = new ol.format.WMSCapabilities();
         const response = await fetch(`${baseUrl}?service=WMS&version=1.3.0&request=GetCapabilities`);
         const text = await response.text();
         const result = parser.read(text);

         if (!result || !result.Capability || !result.Capability.Layer || !result.Capability.Layer.Layer) {
           throw new Error('No layers found in WMS capabilities');
         }

         const layers = result.Capability.Layer.Layer;

         loadedServices[baseUrl] = {
           type: 'wms',
           source: source,
           layers: layers,
           olLayers: {}
         };

         updateLayerList();
       }

       function updateLayerList() {
         if (Object.keys(loadedServices).length === 0) {
           layerListDiv.innerHTML = '<p>No layers loaded yet. Enter a service URL and click "Load Service".</p>';
           return;
         }

         let html = '';

         for (const [serviceUrl, service] of Object.entries(loadedServices)) {
           html += `<div><strong>${serviceUrl}</strong></div>`;

           service.layers.forEach(layer => {
             const layerName = layer.Name;
             const layerTitle = layer.Title || layer.Name;
             const isChecked = service.olLayers[layerName] ? 'checked' : '';

             html += `
               <div class="layer-item">
                 <input type="checkbox" id="${serviceUrl}-${layerName}" ${isChecked} onchange="window.toggleLayer('${serviceUrl}', '${layerName}')">
                 <label for="${serviceUrl}-${layerName}">${layerTitle}</label>
               </div>
             `;
           });
         }

         layerListDiv.innerHTML = html;
       }

       window.toggleLayer = function(serviceUrl, layerName) {
         const service = loadedServices[serviceUrl];
         if (!service) return;

         const checkbox = document.getElementById(`${serviceUrl}-${layerName}`);
         const isChecked = checkbox.checked;

         if (isChecked && !service.olLayers[layerName]) {
           const layer = new ol.layer.Tile({
             source: service.source,
             visible: true,
             name: layerName
           });
           layer.getSource().updateParams({ LAYERS: layerName });
           map.addLayer(layer);
           service.olLayers[layerName] = layer;
         } else if (!isChecked && service.olLayers[layerName]) {
           map.removeLayer(service.olLayers[layerName]);
           delete service.olLayers[layerName];
         }
       };

       map.on('singleclick', async function (evt) {
         featureInfoDiv.innerHTML = 'Loading info...';
         const viewResolution = map.getView().getResolution();

         for (const [serviceUrl, service] of Object.entries(loadedServices)) {
           if (service.type !== 'wms') continue;

           for (const [layerName, layer] of Object.entries(service.olLayers)) {
             if (!layer.getVisible()) continue;

             const url = layer.getSource().getFeatureInfoUrl(
               evt.coordinate,
               viewResolution,
               map.getView().getProjection(),
               { INFO_FORMAT: 'application/json' }
             );

             if (url) {
               try {
                 const response = await fetch(url);
                 if (!response.ok) throw new Error(`Error ${response.status}`);
                 const featureInfo = await response.json();

                 featureInfoDiv.innerHTML = `<pre>${JSON.stringify(featureInfo, null, 2)}</pre>`;
                 return;
               } catch (error) {
                 console.error('GetFeatureInfo Error:', error.message);
                 featureInfoDiv.innerHTML = `<p>Error fetching feature info: ${error.message}</p>`;
               }
             }
           }
         }

         featureInfoDiv.innerHTML = '<p>No feature information available.</p>';
       });

       loadServiceButton.addEventListener('click', loadService);
       serviceUrlInput.addEventListener('keypress', (e) => {
         if (e.key === 'Enter') loadService();
       });
     });
   </script>
