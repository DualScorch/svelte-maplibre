<script lang="ts">
  import MapLibre from '$lib/MapLibre.svelte';
  import CodeSample from '$site/CodeSample.svelte';
  import code from './+page.svelte?raw';
  import type { PageData } from './$types';
  import type { StyleSpecification } from 'maplibre-gl';
  import Marker from '$lib/Marker.svelte';
  import Popup from '$lib/Popup.svelte';
  import { Avatar, ListBox, ListBoxItem, popup, type PopupSettings } from '@skeletonlabs/skeleton';
  import { restaurants } from '$lib/data';

  export let data: PageData;

  type CategoryMap = {
    [key: string]: {
    icon: string;
    color: string;
  };
  };

  const categoryMap: CategoryMap = {
    "Pizza": {
      icon: '🍕',
      color: 'bg-slate-500',
    },
    'Sushi/Japanese': {
      icon: '🇯🇵',
      color: 'bg-gray-400',
    },
    "Chinese": {
      icon: '🇨🇳',
      color: 'bg-zinc-400',
    },
    "Italian": {
      icon: '🇮🇹',
      color: 'bg-neutral-400',
    },
    "Mexican": {
      icon: '🇲🇽',
      color: 'bg-stone-400',
    },
    "Vietnamese": {
      icon: '🇻🇳',
      color: 'bg-red-400',
    },
    "French": {
      icon: '🇫🇷',
      color: 'bg-orange-400',
    },
    "Korean": {
      icon: '🇰🇷',
      color: 'bg-amber-400',
    },
    'Eastern/Central European': {
      icon: '🇪🇺',
      color: 'bg-yellow-400',
    },
    "Seafood": {
      icon: '🦞',
      color: 'bg-lime-400',
    },
    "Thai": {
      icon: '🇹🇭',
      color: 'bg-green-400',
    },
    "Burgers": {
      icon: '🍔',
      color: 'bg-emerald-400',
    },
    'BBQ/Steak': {
      icon: '🥩',
      color: 'bg-teal-400',
    },
    'Asian Fusion': {
      icon: '🍱',
      color: 'bg-cyan-400',
    },
    'East African': {
      icon: '🇪🇹',
      color: 'bg-sky-400',
    },
    'Persian/Afghan': {
      icon: '🇮🇷',
      color: 'bg-blue-400',
    },
    "Georgian": {
      icon: '🇬🇪',
      color: 'bg-indigo-400',
    },
    "Ramen": {
      icon: '🍜',
      color: 'bg-violet-400',
    },
    "Indian": {
      icon: '🇮🇳',
      color: 'bg-purple-400',
    },
    'Vegetarian/Vegan': {
      icon: '🥦',
      color: 'bg-fuchsia-400',
    },
    'Swedish/Nordic': {
      icon: '🇸🇪',
      color: 'bg-pink-400',
    },
    "Sausages": {
      icon: '🌭',
      color: 'bg-slate-400',
    },
    'Fine Dining': {
      icon: '🍽',
      color: 'bg-gray-500',
    },
    'Middle Eastern': {
      icon: '🇸🇦',
      color: 'bg-zinc-500',
    },
    'Latin/South American': {
      icon: '🇦🇷',
      color: 'bg-neutral-500',
    },
    'Food court': {
      icon: '🍽',
      color: 'bg-stone-500',
    },
    "Brunch": {
      icon: '🥞',
      color: 'bg-red-500',
    },
    "Coffee": {
      icon: '☕️',
      color: 'bg-orange-500',
    },
    "Wine": {
      icon: '🍷',
      color: 'bg-amber-500',
    },
    'Craft beer': {
      icon: '🍺',
      color: 'bg-yellow-500',
    },
    "Cocktails": {
      icon: '🍸',
      color: 'bg-lime-500',
    },
    'Dive bar': {
      icon: '🍻',
      color: 'bg-green-500',
    },
    'Outdoor bar': {
      icon: '🍹',
      color: 'bg-emerald-500',
    },
    'Rooftop bar': {
      icon: '🌇',
      color: 'bg-teal-500',
    },
  };

  const mapClasses = 'relative w-full aspect-[9/16] max-h-[70vh] sm:max-h-full sm:aspect-video';

  let filter = '';
  let filterCategory: string | null = null;

  let filteredRestaurants = restaurants;
  $: filteredRestaurants = restaurants.filter((restaurant) => (filterCategory ? restaurant.category == filterCategory : true) && restaurant.name.toLocaleLowerCase().includes(filter.toLocaleLowerCase()));

  const popupCombobox: PopupSettings = {
    event: 'focus-click',
    target: 'popupCombobox',
    placement: 'bottom',
    closeQuery: '.listbox-item'
  };
</script>


<div class="card w-72 shadow-xl py-2 z-10 rounded-md bg-surface-800" data-popup="popupCombobox">
	<ListBox active="bg-surface-600" rounded="rounded-none" class="text-on-surface-token h-[40vh] overflow-y-scroll transition duration-250 ease-in-out bg-surface-800" hover="hover:brightness-150">
    <ListBoxItem bind:group={filterCategory} name="category" value={null} class="bg-opacity-80 group">
      <div class="flex items-center gap-2 group-hover:scale-[1.02] transition duration-150 ease-in-out">
        <span class="text-2xl">🍽</span>
        <span>Alla</span>
      </div>
    </ListBoxItem>
    {#each Object.entries(categoryMap) as [categoryName, category]}
      <ListBoxItem bind:group={filterCategory} name="category" value={categoryName} class="bg-opacity-80 group" >
        <div class="flex items-center gap-2 group-hover:scale-[1.02] transition duration-150 ease-in-out">
          <span class="text-2xl">{category.icon}</span>
          <span>{categoryName}</span>
        </div>
      </ListBoxItem>
    {/each}
	</ListBox>
	<div class="arrow bg-surface-500-400-token" />
</div>


<div class="absolute top-2 right-2 z-10 flex flex-col gap-2">
    <input bind:value={filter} class="input bg-surface-800 py-2 px-4 rounded-md w-72 text-on-secondary-token" type="text" placeholder="Sök restaurang" />
    <button class="btn bg-surface-800 text-on-surface-token w-72 justify-between rounded-md" use:popup={popupCombobox}>
      <span class="capitalize">{filterCategory ?? ""} {filterCategory ? categoryMap[filterCategory].icon : "Alla 🍽"}</span>
      <span>↓</span>
    </button>
</div>

<MapLibre
  style="https://api.maptiler.com/maps/streets-v2/style.json?key=XvjcZuXFkP2hOyz114Er"
  standardControls
  zoom={13}
  center={[18.07, 59.325]}
  maxBounds={[[17.82, 59.2573], [18.32, 59.3927]]}
>
  {#each filteredRestaurants as restaurant (restaurant.id)}
  {@const category = categoryMap[restaurant.category]}
    {#if restaurant.lng && restaurant.lat}
      <Marker
        lngLat={{
          lng: restaurant.lng,
          lat: restaurant.lat,
        }}
        class="border-gray-200 border shadow-2xl text-lg focus:outline-2 focus:outline-black w-8 h-8 {category.color} text-black rounded-full grid place-items-center"
      >
        <span>
          {category.icon}
        </span>

        <Popup openOn="click" offset={[0, -10]}>
          <div class=" bg-white text-on-primary-token flex justify-center items-center">
            <span>{restaurant.name} {restaurant.category}</span>
          </div>
        </Popup>
      </Marker>
    {/if}
  {/each}
</MapLibre>
