<script lang="ts">
    import MapLibre from '$lib/MapLibre.svelte';
    import GeoJSON from '$lib/GeoJSON.svelte';
    import Popup from '$lib/Popup.svelte';
    import MarkerLayer from '$lib/MarkerLayer.svelte';
    import quakeImageUrl from '$site/earthquake.png';
    import tsunamiImageUrl from '$site/tsunami.png';
    import restaurants from '$site/restaurants.geojson?url';
  
    let clickedFeature: Record<string, any> | null = null;
  
    let openOn: 'click' | 'hover' = 'hover';
  </script>
  
  <MapLibre
    style="https://basemaps.cartocdn.com/gl/positron-gl-style/style.json"
    standardControls
  >
    <GeoJSON
      id="earthquakes"
      data={restaurants}
      cluster={{
        radius: 1000,
        maxZoom: 15,
      }}
    >
      <MarkerLayer
        applyToClusters
        interactive
        on:click={(e) => (clickedFeature = e.detail.feature?.properties)}
        let:feature
      >
        U
        <Popup {openOn} closeOnClickInside>
          {feature}
        </Popup>
      </MarkerLayer>
  
      <MarkerLayer
        applyToClusters={false}
        on:click={(e) => (clickedFeature = e.detail.feature?.properties)}
        let:feature
      >
      <div class="bg-surface-700 w-fit rounded-md px-1 py-0.5 text-xs bg-opacity-75">
        <!-- {#each Array(Math.floor((Math.random() * 5)) + 1) as _}
        🌟
        {/each} -->
      </div>
      <span class=" w-8 h-8 grid place-items-center border bg-opacity-75 rounded-full">
        A
      </span>
        <Popup {openOn} closeOnClickInside>
          p
        </Popup>
      </MarkerLayer>
    </GeoJSON>
  </MapLibre>
  